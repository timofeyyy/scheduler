import json

from sentence_transformers import SentenceTransformer, util
import torch
from sqlalchemy import inspect
from translate import Translator

from scheduler.db import Microchips, Resistors, Transistors, Diods, Capacitors
from scheduler.settings import get_settings

print("загружается модель SentenceTransformer")
model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
print("модель загружена")


class ColumnClassifier:

    def __init__(self):
        settings = get_settings()
        self.path_to_alternatives = settings["classifier"]["cached"]
        self.alternatives = self.read()

    def edit_columns(self, db_oim_model_type, alternatives=None):
        if alternatives is None:
            alternatives = []
        tablename = db_oim_model_type.__tablename__
        mapper = inspect(db_oim_model_type)
        if self.alternatives.get(tablename) is None:
            self.alternatives[tablename] = {}
        for attr in mapper.attrs:
            if getattr(attr, "columns", None) and attr.columns[0].info.get("skip"):
                continue
            if self.alternatives[tablename].get(attr.key) is None:
                self.alternatives[tablename][attr.key] = []

    def save(self):
        with open(self.path_to_alternatives, 'w') as file:
            json.dump(self.alternatives, file, indent=1)

    def read(self):
        with open(self.path_to_alternatives, 'r') as file:
            try:
                return json.load(file)
            except:
                return {}

    def classify(self, data: dict, to_eng: 0 | 1 | 2):
        for component_type in data.keys():
            corpus = []
            original_columns: list = self.alternatives[component_type].keys()
            taken_columns = []
            for original_column in original_columns:
                corpus.append(original_column)
            print(f"{component_type}\n{corpus}\n\n")
            component_type_alternative_columns: dict = data[component_type]
            corpus_emb = model.encode(corpus, convert_to_tensor=True)
            for column in component_type_alternative_columns.keys():
                input_value = column
                if to_eng == 1:
                    translator = Translator(from_lang="russian", to_lang="english")
                    input_value = translator.translate(column)
                query_emb = model.encode(input_value, convert_to_tensor=True)
                sims = util.cos_sim(query_emb, corpus_emb)[0]
                max_sim, max_idx = torch.max(sims, dim=0)
                threshold = 0.6
                if max_sim >= threshold:
                    column_print =  f"{column}/{input_value}" if to_eng == 1 else f"{column}"
                    print(f"'{column_print}' похоже на '{corpus[max_idx]}' (similarity={max_sim:.2f})")
                    # probs = torch.softmax(sims, dim=0)
                    # for i, word in enumerate(corpus):
                    #     print(f"{word}: {probs[i]:.3f}")

                    # if corpus[max_idx] not in taken_columns:
                    #     pass
                    taken_columns.append(corpus[max_idx])
                else:
                    print(f"'{column}/{input_value}' не относится (similarity={max_sim:.2f})")
                # print("\n\n\n")



cc = ColumnClassifier()
# cc.get_actual_columns(db_oim_model_type=Microchips)
# cc.get_actual_columns(db_oim_model_type=Resistors)
# cc.get_actual_columns(db_oim_model_type=Transistors)
# cc.get_actual_columns(db_oim_model_type=Diods)
# cc.get_actual_columns(db_oim_model_type=Capacitors)
# cc.save()

ru_test = {
    Microchips.__tablename__: {
        "Серия": "23K",
        "Тип памяти": "SRAM",
        "Объем памяти":	"256 Кбит(32К x 8)",
        "Максимальная тактовая частота (скорость)":	"20 МГц",
        "Интерфейс": "spi",
        "Напряжение питания, В": "2.7…3.6",
        "Рабочая температура, °C":	"-40…+85",
        "Корпус": "SOIC-8(3.90мм)",
        "Вес, г": "0.15",

        # "Серия:": "23K",
        # "Тип памяти:": "SRAM",
        # "Объем памяти:":	"256 Кбит(32К x 8)",
        # "Максимальная тактовая частота (скорость):":	"20 МГц",
        # "Интерфейс:": "spi",
        # "Напряжение питания, В:": "2.7…3.6",
        # "Рабочая температура, °C:":	"-40…+85",
        # "Корпус:": "SOIC-8(3.90мм)",
        # "Вес, г:": "0.15"
    }
}

# cc.classify(data=ru_test, to_eng=1)
cc.classify(data=ru_test, to_eng=0)



#
# corpus = ["MinOperatingTemperature", "MaxOperatingTemperature", "Package", "QualicationSG", "MaxPermissibleDCVoltage"]
#
# # new_word1 = "минимальная температура"
# # new_word2 = "максимальная температура"
# # new_word3 = "МИН температура"
# # new_word4 = "МАКС температура"
# new_word1 = "корпус"
# new_word2 = "ток"
# new_word3 = "напряжение"
# new_word4 = "ерунда"
#
# translator = Translator(from_lang="russian", to_lang="english")
# new_word_en1 = translator.translate(new_word1)
# new_word_en2 = translator.translate(new_word2)
# new_word_en3 = translator.translate(new_word3)
# new_word_en4 = translator.translate(new_word4)
#
# corpus_emb = model.encode(corpus, convert_to_tensor=True)
# query_emb1 = model.encode(new_word_en1, convert_to_tensor=True)
# query_emb2 = model.encode(new_word_en2, convert_to_tensor=True)
# query_emb3 = model.encode(new_word_en3, convert_to_tensor=True)
# query_emb4 = model.encode(new_word_en4, convert_to_tensor=True)
#
# query_emb5 = model.encode(new_word1, convert_to_tensor=True)
# query_emb6 = model.encode(new_word2, convert_to_tensor=True)
# query_emb7 = model.encode(new_word3, convert_to_tensor=True)
# query_emb8 = model.encode(new_word4, convert_to_tensor=True)
#
# queries = [
#     [query_emb1, new_word_en1], [query_emb2, new_word_en2], [query_emb3, new_word_en3], [query_emb4, new_word_en4],
#     [query_emb5, new_word1], [query_emb6, new_word2], [query_emb7, new_word3], [query_emb8, new_word4]
# ]
#
# for query in queries:
#
#     sims = util.cos_sim(query[0], corpus_emb)[0]
#     max_sim, max_idx = torch.max(sims, dim=0)
#
#     threshold = 0
#
#     if max_sim >= threshold:
#         print(f"'{query[1]}' похоже на '{corpus[max_idx]}' (similarity={max_sim:.2f})")
#
#         probs = torch.softmax(sims, dim=0)
#         for i, word in enumerate(corpus):
#             print(f"{word}: {probs[i]:.3f}")
#     else:
#         print(f"'{query[1]}' не относится (max similarity={max_sim:.2f})")
#     print("\n\n\n")
#
#
