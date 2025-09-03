from sqlalchemy.orm import Session
from db import Technologies
from translate import Translator
from .family import ComponentReferenceFamily


class TechnologyRepo(ComponentReferenceFamily):

    def __init__(self, engine):
        self.engine = engine

    def get_id_by_value(self, ru_name):
        with Session(autoflush=False, bind=self.engine) as db:
            technology = db.query(Technologies).filter(Technologies.RuTechnologyName == ru_name).first()
            if technology is None:
                technology = Technologies()
                technology.RuTechnologyName = ru_name
                translator = Translator(from_lang="russian", to_lang="english")
                translation = translator.translate(ru_name)
                technology.EnTechnologyName = translation
                db.add(technology)
                db.commit()
            return technology.ID
