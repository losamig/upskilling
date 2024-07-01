from semantic_kernel.functions import kernel_function
import json
from typing import Annotated

class CarAPI:
    """
    Description:  provides a set of functions to interact with different systems available in a car.
    """

    @kernel_function(description="sets the positions of individual windows of the car", name="windows_actions")
    def windows_position(
        self,
        action: Annotated[str, "the operation to perform on the windows"],
        target_window: Annotated[str, "window that is targeted by the operation"],
    ) -> Annotated[str, "the description of the operation that has been performed"]:
        message = f"Executing {action} on window {target_window}"
        print(message)
        return message
    
    @kernel_function(description="Operates the aircon of the car to adjust temperature", name="aircon")
    def aircon_temperature(
        self,
        temperature: Annotated[float, "the new temperature"],
    ) -> Annotated[str, "the description of the operation that has been performed"]:
        message = f"Setting aircon to {temperature}"
        print(message)
        return message
        
    @kernel_function(description="Returns the status of the the car", name="GetCarStatus")
    def get_car_status(
        self
    ) -> Annotated[str, "json document with the status of the car"]:
        print("Reading car status")
        car_status = {
            "car_windows_status": [
                {
                    "window": "front_left",
                    "status": "closed",
                },
                {
                    "window": "front_right",
                    "status": "closed",
                },
                {
                    "window": "rear_left",
                    "status": "open",
                },
                {
                    "window": "rear_right",
                    "status": "open",
                }
            ]
        }
        return json.dumps(car_status, indent=4)
    
        