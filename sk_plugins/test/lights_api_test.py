
import unittest
import sys
sys.path.append('../../') #needed to get util in the path
sys.path.append('../lights_plugin/') 
from lights_plugin import LightsPlugin
from util.house import House, LightStatus


class TestLightsApi(unittest.TestCase):
    

    def test_get_light(self):
        api = LightsPlugin()       
        House().reset() 
        self.assertEqual(api.get_light('LIVINGROOM'), 'The lights of the room Room.LIVINGROOM are LightStatus.OFF', "incorrect light status")

    def test_get_light_by_unknown_room(self):
        api = LightsPlugin()        
        House().reset() 
        self.assertEqual(api.get_light('SWIMMINGPOOL'), "Room SWIMMINGPOOL not found", "incorrect light status")

    def test_change_light(self):
        api = LightsPlugin()       
        House().reset() 
        api.change_light('LIVINGROOM','ON') 
        self.assertEqual(api.get_light('LIVINGROOM'), 'The lights of the room Room.LIVINGROOM are LightStatus.ON', "incorrect light status")



if __name__ == '__main__':
    unittest.main()