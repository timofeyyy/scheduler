from abc import *


class ComponentReferenceFamily(ABC):
    @abstractmethod
    def get_id_by_value(self, value): pass
