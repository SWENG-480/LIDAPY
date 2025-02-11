#LIDA Cognitive Framework
#Pennsylvania State University, Course : SWENG480
#Authors: Katie Killian, Brian Wachira, and Nicole Vadillo
from src.ActionSelection.ActionSelectionAdapter import ActionSelectionAdapter
from src.ModuleObserver.ModuleNotifier import ModuleNotifier


class ProceduralMemory:
    def __init__(self, action_selection=None):
        self.percept = None
        self.action_selection = action_selection
        self.schemes = {} # initialize empty memory for schemes
        self.observer = ActionSelectionAdapter()
        self.notifier = ModuleNotifier()
        self.notifier.add_observer(self.observer)

    def add_scheme(self, percept, action):
        self.schemes[percept] = action # add new scheme to memory
        # percept: percept cue ("goal", "safe", or "danger")
        # action: corresponding action or scheme

    def get_action(self, percept):
        return self.schemes.get(percept, None) # get action for the percept
        # return corresponding action or None if not found

    def notify(self, percept):
        self.percept = percept["Percept"]
        self.add_scheme(self.percept, percept["Action"])
        self.observer.notify(percept, self.action_selection)