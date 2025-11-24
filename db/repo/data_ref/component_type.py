from sqlalchemy import func
from sqlalchemy.orm import Session
from ..db_oim_orm import ComponentTypes
from translate import Translator
from .family import DataRefFamilyLang


class ComponentTypeRepo(DataRefFamilyLang):

    def get_obj_by_en_value(self, value):
        with Session(autoflush=False, bind=self.engine) as db:
            component_type: ComponentTypes = db.query(ComponentTypes).filter(func.lower(ComponentTypes.EnComponentType) == value.lower()).first()
            if component_type is None:
                component_type = ComponentTypes()
                component_type.EnComponentType = value
                translator = Translator(from_lang="english", to_lang="russian")
                translation = translator.translate(value)
                component_type.RuComponentType = translation
                db.add(component_type)
                db.commit()
                db.refresh(component_type)
            db.expunge(component_type)
            # print(f"component_type.ID = {component_type.ID}")
            return component_type

    def __init__(self, engine):
        self.engine = engine
        self.records = []

    def select(self):
        with Session(autoflush=False, bind=self.engine) as db:
            return db.query(ComponentTypes).all()

    def get_obj_by_ru_value(self, value):
        with Session(autoflush=False, bind=self.engine) as db:
            component_type: ComponentTypes = db.query(ComponentTypes).filter(func.lower(ComponentTypes.RuComponentType) == value.lower()).first()
            if component_type is None:
                component_type = ComponentTypes()
                component_type.RuComponentType = value
                translator = Translator(from_lang="russian", to_lang="english")
                translation = translator.translate(value)
                component_type.EnComponentType = translation
                db.add(component_type)
                db.commit()
                db.refresh(component_type)
            db.expunge(component_type)
            # print(f"component_type.ID = {component_type.ID}")
            return component_type
