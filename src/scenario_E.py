# fabrick

# Fabrications d'instances

import abc
from typing import Literal

class AbstractPlayable(metaclass = abc.ABCMeta):
    def __init__(self, **kwargs):
        pass

    @abc.abstractmethod
    def attaquer(self) -> None:
        raise NotImplementedError

class Guerrier(AbstractPlayable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def attaquer(self) -> None:
        print("Guerrier attaque")

class Magicien(AbstractPlayable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def attaquer(self) -> None:
        print("Magicien attaque")

class Archer(AbstractPlayable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def attaquer(self) -> None:
        print("Archer attaque")

class Factory:
    def __init__(self):
        pass

    @staticmethod
    def create(type: Literal['Guerrier', 'Magicien', 'Archer'], **kwargs) -> AbstractPlayable:
        match type:
            case 'Guerrier':
                return Guerrier(**kwargs)
        
            case 'Magicien':
                return Magicien(**kwargs)
        
            case 'Archer':
                return Archer(**kwargs)
            
            case _:
                raise ValueError("Invalid type")