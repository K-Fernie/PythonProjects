"""Peasant class to create a peasant object that will be used to determine game progress"""

class Peasant:
    """
    Peasant class holds user data for the story progression, this can be saved for re-load
    """ 
    def __init__(self, storyframe, inventory, stink, dress, fire):
        self.storyframe = storyframe #(i.e. A1, A2, A3, A4)
        self.inventory = inventory
        self.stink = stink
        self.dress = dress
        self.fire = fire


class Objectives:
    """
    The objective class holds a copy of the objective dictionary, this is used for deepcopying 
    from internal data when the player dies and needs to re-start
    """
    def __init__(self, objective_dict):
        self.objective_dict = objective_dict