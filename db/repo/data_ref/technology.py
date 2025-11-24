from sqlalchemy import func
from sqlalchemy.orm import Session
from ..db_oim_orm import Technologies
from translate import Translator
from .family import DataRefFamilyLang


class TechnologyRepo(DataRefFamilyLang):

    def get_obj_by_en_value(self, value):
        with Session(autoflush=False, bind=self.engine) as db:
            technology: Technologies = db.query(Technologies).filter(func.lower(Technologies.EnTechnologyName) == value.lower()).first()
            if technology is None:
                technology = Technologies()
                technology.EnTechnologyName = value
                translator = Translator(from_lang="english", to_lang="russian")
                translation = translator.translate(value)
                technology.RuTechnologyName = translation
                db.add(technology)
                db.commit()
                db.refresh(technology)
            db.expunge(technology)
            # print(f"technology.ID = {technology.ID}")
            return technology

    def select(self):
        pass

    def __init__(self, engine):
        self.engine = engine

    def get_obj_by_ru_value(self, value):
        with Session(autoflush=False, bind=self.engine) as db:
            technology: Technologies = db.query(Technologies).filter(func.lower(Technologies.RuTechnologyName) == value.lower()).first()
            if technology is None:
                technology = Technologies()
                technology.RuTechnologyName = value
                translator = Translator(from_lang="russian", to_lang="english")
                translation = translator.translate(value)
                technology.EnTechnologyName = translation
                db.add(technology)
                db.commit()
                db.refresh(technology)
            db.expunge(technology)
            # print(f"technology.ID = {technology.ID}")
            return technology
