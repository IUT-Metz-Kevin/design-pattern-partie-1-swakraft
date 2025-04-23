# Adapter

# Ajoute la compatibilité entre les interfaces

import abc

# classes de controlleurs
class Keyboard:
    def espace(self) -> None:
        pass

    def right_click(self) -> None:
        pass

    def left_click(self) -> None:
        pass

class Xbox:
    def button_A(self) -> None:
        pass

    def button_B(self) -> None:
        pass

    def button_X(self) -> None:
        pass

class PS5:
    def button_cross(self) -> None:
        pass

    def button_circle(self) -> None:
        pass

    def button_triangle(self) -> None:
        pass

# classe de contrôles du jeu
class ControlerActions(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def jump(self) -> None:
        pass

    @abc.abstractmethod
    def attack(self) -> None:
        pass

    @abc.abstractmethod
    def interact(self) -> None:
        pass

# classes d'adaptateurs
class KeyboardWrapper(ControlerActions):
    __slots__ = 'controller',
    def __init__(self, controller: Keyboard):
        self.controller = controller
    
    def jump(self) -> None:
        self.controller.espace()
    
    def attack(self) -> None:
        self.controller.right_click()
    
    def interact(self) -> None:
        self.controller.left_click()

class XboxWrapper(ControlerActions):
    __slots__ = 'controller',
    def __init__(self, controller: Xbox):
        self.controller = controller
    
    def jump(self) -> None:
        self.controller.button_A()
    
    def attack(self) -> None:
        self.controller.button_B()
    
    def interact(self) -> None:
        self.controller.button_X()

class PS5Wrapper(ControlerActions):
    __slots__ = 'controller',
    def __init__(self, controller: PS5):
        self.controller = controller
    
    def jump(self) -> None:
        self.controller.button_cross()
    
    def attack(self) -> None:
        self.controller.button_circle()
    
    def interact(self) -> None:
        self.controller.button_triangle()