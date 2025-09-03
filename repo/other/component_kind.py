from sqlalchemy.orm import Session
from translate import Translator
from db import ComponentKinds
from .family import ComponentReferenceFamily


class ComponentKindRepo(ComponentReferenceFamily):

    def __init__(self, engine):
        self.engine = engine

    def get_id_by_value(self, ru_name):
        with Session(autoflush=False, bind=self.engine) as db:
            kind = db.query(ComponentKinds).filter(ComponentKinds.RuComponentKind == ru_name).first()
            if kind is None:
                kind = ComponentKinds()
                kind.RuComponentKind = ru_name
                translator = Translator(from_lang="russian", to_lang="english")
                translation = translator.translate(ru_name)
                kind.EnComponentKind = translation
                db.add(kind)
                db.commit()
            return kind.ID
