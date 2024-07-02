from enum import Enum

Room = Enum('Room', ['LIVINGROOM', 'KITCHEN', 'BEDROOM', 'BATHROOM'])
LightStatus = Enum('LightStatus', ['ON', 'OFF'])

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class House(metaclass=Singleton):   
   def __init__(self) -> None:
       self.reset()
       
   def reset(self):
        self.status = {
            Room.LIVINGROOM: LightStatus.OFF,
            Room.KITCHEN: LightStatus.OFF,
            Room.BEDROOM: LightStatus.OFF,
            Room.BATHROOM: LightStatus.OFF
        }     

