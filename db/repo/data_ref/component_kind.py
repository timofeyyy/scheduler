from sqlalchemy import func
from sqlalchemy.orm import Session
from translate import Translator

from ..db_oim_orm import ComponentKinds
from .family import DataRefFamilyLang


class ComponentKindRepo(DataRefFamilyLang):
    def get_obj_by_en_value(self, value):
        with Session(autoflush=False, bind=self.engine) as db:
            kind: ComponentKinds = db.query(ComponentKinds).filter(func.lower(ComponentKinds.EnComponentType) == value.lower()).first()
            if kind is None:
                kind = ComponentKinds()
                kind.EnComponentKind = value
                translator = Translator(from_lang="english", to_lang="russian")
                translation = translator.translate(value)
                kind.RuComponentKind = translation
                db.add(kind)
                db.commit()
                db.refresh(kind)
            db.expunge(kind)
            # print(f"kind.ID = {kind.ID}")
            return kind

    def select(self):
        pass

    def __init__(self, engine):
        self.engine = engine

    def get_obj_by_ru_value(self, value):
        with Session(autoflush=False, bind=self.engine) as db:
            kind: ComponentKinds = db.query(ComponentKinds).filter(func.lower(ComponentKinds.RuComponentKind) == value.lower()).first()
            if kind is None:
                kind = ComponentKinds()
                kind.RuComponentKind = value
                translator = Translator(from_lang="russian", to_lang="english")
                translation = translator.translate(value)
                kind.EnComponentKind = translation
                db.add(kind)
                db.commit()
                db.refresh(kind)
            db.expunge(kind)
            # print(f"kind.ID = {kind.ID}")
            return kind
