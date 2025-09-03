from sqlalchemy.orm import Session
from db import ComponentTypes
from translate import Translator
from .family import ComponentReferenceFamily


class ComponentTypeRepo(ComponentReferenceFamily):

    def __init__(self, engine):
        self.engine = engine

    def get_id_by_value(self, ru_name):
        with Session(autoflush=False, bind=self.engine) as db:
            type = db.query(ComponentTypes).filter(ComponentTypes.RuComponentType == ru_name).first()
            if type is None:
                type = ComponentTypes()
                type.RuComponentType = ru_name
                translator = Translator(from_lang="russian", to_lang="english")
                translation = translator.translate(ru_name)
                type.EnComponentType = translation
                db.add(type)
                db.commit()
            return type.ID
