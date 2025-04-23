# Decorateur

# Enrichit une classe 'de base'

import abc

class Boisson(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def description(self) -> str:
        pass

    @abc.abstractmethod
    def prix(self) -> float:
        pass

class Cafe(Boisson):
    def description(self) -> str:
        return "Café"
    
    def prix(self) -> float:
        return 4

class Supplement(Boisson):
    def __init__(self, boisson: Boisson):
        self.boisson = boisson

class Lait(Supplement):
    def description(self) -> str:
        return self.boisson.description() + ", lait"
    
    def prix(self) -> float:
        return self.boisson.prix() + 1

class LaitDeCoco(Supplement):
    def description(self) -> str:
        return self.boisson.description() + ", lait de coco"
    
    def prix(self) -> float:
        return self.boisson.prix() + 2

class Chantilly(Supplement):
    def description(self) -> str:
        return self.boisson.description() + ", chantilly"
    
    def prix(self) -> float:
        return self.boisson.prix() + 1

class SaveurVanille(Supplement):
    def description(self) -> str:
        return self.boisson.description() + ", saveur vanille"
    
    def prix(self) -> float:
        return self.boisson.prix() + 0.5

class Sucre(Supplement):
    def description(self) -> str:
        return self.boisson.description() + ", sucre"
    
    def prix(self) -> float:
        return self.boisson.prix()