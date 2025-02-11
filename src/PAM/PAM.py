#LIDA Cognitive Framework
#Pennsylvania State University, Course : SWENG480
#Authors: Katie Killian, Brian Wachira, and Nicole Vadillo

"""
Responsible for storing and retrieving associations between perceptual
elements. Interacts with Sensory Memory, Situational Model, and Global Workspace.
Input: Sensory Stimuli and cues from Sensory Memory
Output: Local Associations, passed to others
"""
from src.ModuleObserver.ModuleNotifier import ModuleNotifier as Notifier
from src.ProceduralMemory.ProceduralMemAdapter import ProceduralMemAdapter


class PerceptualAssociativeMemory:
    def __init__(self, procedural_memory):
        #Storing associations
        self.associations = {}
        self.procedural_memory = procedural_memory
        self.observer = ProceduralMemAdapter()
        self.notifier = Notifier()
        self.notifier.add_observer(self.observer)
        self.state = None
        self.surrounding_tiles = None
        self.position = None
        self.action = None
        self.percept = None
        self.action_value= {
            "3": "up",
            "2": "right",
            "1": "down",
            "0": "left",
        }

    def notify(self, event):
        self.state = event["state"]
        self.surrounding_tiles = event["surrounding_tiles"]
        self.action = event["action"]
        self.get_position(self.state)
        self.learn(self.state, self.surrounding_tiles, self.action)

    def get_position(self, state):
        if state < 4:
            self.position = [0, state]
        elif 3 < state < 8:
            self.position = [1, state - 3]
        elif 7 < state < 12:
            self.position = [2, state - 7]
        elif 11 < state < 16:
            self.position = [3, state - 11]
        return self.position

    def add_association(self, cue, pattern):
        #Add new associations
        if self.associations.__eq__(None) or cue not in self.associations:
            self.associations[pattern] = []
        self.associations[pattern].append(cue)
        return pattern

    def retrieve_associations(self, cue):
        #Retreiving associations for the given cue
        if not self.associations.__eq__(None) and cue in self.associations:
            return self.associations[cue]
        else:
            # create default association
            pattern = self.add_association(cue,
                                           f"default-pattern-{cue}")
            return self.associations[pattern]

    def learn(self, state, outcome, action):
        if outcome[self.action_value[str(action)]] == "G":
            self.percept = self.add_association("Move " + self.action_value[
                                                    str(action)] + ","
                                                        " Current state: " +
                                                str(state), "goal")
        elif outcome[self.action_value[str(action)]] == "H":
            self.percept = self.add_association("Move " + self.action_value[
                                                    str(action)] + ","
                                                        " Current state: " +
                                                str(state), "danger")
        elif outcome[self.action_value[str(action)]] == "S":
            self.percept = self.add_association("Move " + self.action_value[
                                                    str(action)] + ","
                                                        " Current state: " +
                                                str(state), "start")
        else:
            self.percept = self.add_association("Move " + self.action_value[
                                                    str(action)] + ","
                                                        " Current state: " +
                                                str(state), "safe")

        # Notify Procedural Memory of the outcome
        action_event = {"Current State":
                            self.retrieve_associations("Move " +
                                                       self.action_value
                                                            [str(self.action)]
                                                            +
                                       ", Current state: " +  str(state)),
                        "Percept": self.percept,
                        "Action": self.action,
                        "Position": self.position,
                        "State": state
                        }
        self.observer.notify(action_event, self.procedural_memory)

    """
    NEED: to connect to sensory memory, use data as cue for PAM
    Possible implement of function that can extract patterns
    """

    """
    NEED: To communication with the situational Model
    Passes patterns or local associations for updates to Current Situational Model
    """

    """
    NEED: Implement the Perceptual Learning 
    """