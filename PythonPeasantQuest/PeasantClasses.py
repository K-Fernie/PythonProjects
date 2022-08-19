"""Peasant class to create a peasant object that will be used to determine game progress"""

class Peasant: 

    def __init__(self, name, storyframe, inventory, stink, dress, fire): 
        self.name = name
        self.storyframe = storyframe #(i.e. A1, A2, A3, A4)
        self.inventory = inventory
        self.stink = stink
        self.dress = dress
        self.fire = fire


class Objectives: 
    
    def __init__(self, objectiveDict):
        self.objectiveDict = objectiveDict