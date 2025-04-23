# Composite

# Hierarchie de classes

import abc
from typing import Any, Optional

class AbstractDept(metaclass = abc.ABCMeta):
    __slots__ = '_name',

    def __init__(self, name: str):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name
    
    @property
    @abc.abstractmethod
    def json(self) -> dict[str, Any]:
        raise NotImplementedError

    @abc.abstractmethod
    def add_sous_departement(self, sous_departement: 'Departement'):
        raise NotImplementedError

class Departement(AbstractDept):
    __slots__ = AbstractDept.__slots__ + ('_sous_departements',)
    def __init__(self, name, sous_departements: Optional[list['Departement']] = None):
        super().__init__(name)
        self.sous_departements = sous_departements or []
    
    @property
    def sous_departements(self):
        return self._sous_departements.copy()
    
    @sous_departements.setter
    def sous_departements(self, sous_departements: list['Departement']):
        self._sous_departements = sous_departements
    
    def add_sous_departement(self, sous_departement: 'Departement'):
        self.sous_departements.append(sous_departement)
    
    @property
    def json(self):
        return {
            'name': self.name,
            'sous_departements': [sous_departement.json for sous_departement in self.sous_departements]
        }

root = Departement("Direction Générale", [
    Departement("Secretariat général"),
    Departement("Département technique", [
        Departement("IT"),
        Departement("Web")
    ]),
    Departement("Département commercial", [
        Departement("Achats"),
        Departement("Vente")
    ]),
    Departement("Département financier", [
        Departement("RH"),
        Departement("Comptabilité"),
        Departement("Administration")
    ])
])