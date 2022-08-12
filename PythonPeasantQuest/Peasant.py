#Class to create the peasant object that will be saved in a file

class Peasant: 

    def __init__(self, name, storyframe, inventory, stink, dress, fire): 
        self.name = name
        self.storyframe = storyframe #(i.e. A1, A2, A3, A4)
        self.inventory = inventory
        #Boolean status elements to determine if the peasant is ready to defeat trogdor
        self.stink = stink
        self.dress = dress
        self.fire = fire
