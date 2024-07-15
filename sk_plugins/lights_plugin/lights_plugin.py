from semantic_kernel.functions import kernel_function
import json
from util.house import House, LightStatus, Room

from typing import Annotated

class LightsPlugin:
    """
    Description:  API to act in the lights of a house.    
    """
    @kernel_function(description="changes the light status for a room in the house", name="change_light")
    def change_light(self, 
                   room: Annotated[str, "the operation to perform on the windows"],
                   new_status: Annotated[str, "the operation to perform on the windows"]
    )->  Annotated[str, "the the new status of the lights of the house"]:
        # Convert the room to the enum
        print(f"Changing light status for {room} to {new_status}")
        try:
            room = Room[room.upper()]
        except:
            return f"Room {room} not found"
        try:
            new_status = LightStatus[new_status.upper()]
        except:
            return f"Status {new_status} not found"
        
        House().status[room] = new_status
        return f"Setting light status for {room} to {new_status}"

    @kernel_function(description="gets the light status for a room in the house", name="get_light")
    def get_light(self, 
                   room: Annotated[str, "the room for which to get the light status"]
    )->  Annotated[str, "the the  status of the lights of the requested room"]:        
        try:
            room = Room[room.upper()]
        except:
            return f"Room {room} not found"
        return f"The lights of the room {room} are {House().status[room]}"
    

    
        