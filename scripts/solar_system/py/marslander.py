from dataclasses import dataclasses

@dataclasses
class Marslander:
    length : int = 6
    width: float = 1.56
    weight: int = 360 
    deckHeight: tuple(83,108)
    robotArmLength: float = 1.8
    numberOfSolarPanels: int = 2 
    
#

new_lander = Marslander