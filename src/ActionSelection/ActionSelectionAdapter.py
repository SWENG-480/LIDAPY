from src.ModuleObserver.ModuleObserver import ModuleObserver

class ActionSelectionAdapter(ModuleObserver):

    def __init__(self):
        super().__init__()

    def notify(self, outcome, module):
        module.notify(outcome)