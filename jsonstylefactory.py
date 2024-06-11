from abc import ABC,abstractmethod
class AbstractjsonFactory(ABC):
    @abstractmethod
    def create(self,rootnode):
        pass

    