from abc import ABC, abstractmethod

class Validator(ABC):
    @abstractmethod
    def is_valid(self):
        pass

    @abstractmethod
    def field_name(self):
        pass
