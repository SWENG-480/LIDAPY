#LIDA Cognitive Framework
#Pennsylvania State University, Course : SWENG480
#Authors: Katie Killian, Brian Wachira, and Nicole Vadillo

#from Environment import Environment as env
from src.ModuleObserver.ModuleNotifier import ModuleNotifier
from src.ModuleObserver.ModuleObserver import ModuleObserver
from src.PAM.PAMAdapter import PAMAdapter

"""
This module can temporarily store sensory data from the environment and then
process and transfer to further working memory.
"""

class SensoryMemory:
    def __init__(self, environment=None, pam=None, agent=None):
        self.listeners = [] #initializing listener class
        self.environment = environment  # store environment reference
        self.pam = pam # reference to perceptual associative memory
        self.notifier = ModuleNotifier()
        self.observer = PAMAdapter()
        self.state = None

    def notify(self, state):
        self.state = state

    def run_sensors(self, state=None, col=None, row=None, agent=None):
        """All sensors associated will run with the memory"""
        #Logic to gather information from the environment
        #Example: Reading the current state or rewards
        if state is None:
            # Use environment instance to reset
            state, info, surrounding_tiles, col, row = (self.environment.
                                                        reset(self))
        else:
            col, row = self.environment.col, self.environment.row

        surrounding_tiles = (self.environment.
                             get_surrounding_tiles(self.environment.row,
                                                   self.environment.col))

        action = self.environment.action_space.sample()
        event = {"state": state, "surrounding_tiles": surrounding_tiles,
                 "action": action}

        #Notify PAM of agent's current state and surrounding tiles
        self.observer.notify(event, self.pam)
        #return state, action, surrounding_tiles, col, row

    def get_sensory_content(self, state, outcome, modality=None, params=None):
        """
        Returning the content from this Sensory Memory
        :param modality: Specifying the modality
        :param params: optional parameters to filter or specify the content
        :return: content corresponding to the modality
        """
        self.pam.learn(state, outcome)
        #Logic to retrieve and return data based on the modality.
        return {"modality": modality, "params": params}