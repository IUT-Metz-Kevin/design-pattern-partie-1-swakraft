# Singleton

# Une seule instance partégée

from typing import Optional

class GameSettings:
    __slots__ = 'graphics', 'audio', 'gameplay'
    _instance: Optional['GameSettings'] = None

    class Graphics:
        __slots__ = 'screen_resolution', 'quality'
    
    class Audio:
        __slots__ = 'music_volume', 'sound_volume'

    class Gameplay:
        __slots__ = 'difficulty', 'language'
    
    def __init__(self, *args, **kwargs):
        self.graphics = self.Graphics(*args, **kwargs)
        self.audio = self.Audio(*args, **kwargs)
        self.gameplay = self.Gameplay(*args, **kwargs)
    
    @classmethod
    def get_current(cls) -> 'GameSettings':
        if not cls._instance:
            print("nouvelle instance")
            cls._instance = cls()

        return cls._instance

instance = GameSettings.get_current()
instance = GameSettings.get_current()
instance = GameSettings.get_current()
instance = GameSettings.get_current()