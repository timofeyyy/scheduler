from abc import *


class DataRefFamilyBase(ABC):
    @abstractmethod
    def select(self): pass


class DataRefFamily(DataRefFamilyBase):
    @abstractmethod
    def get_obj_by_value(self, value): pass


class DataRefFamilyLang(DataRefFamilyBase):
    @abstractmethod
    def get_obj_by_ru_value(self, ru_value): pass
    @abstractmethod
    def get_obj_by_en_value(self, en_value): pass
