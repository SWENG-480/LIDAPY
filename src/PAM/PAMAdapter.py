from src.ModuleObserver.ModuleObserver import ModuleObserver


class PAMAdapter(ModuleObserver):
    def __init__(self):
        super().__init__()

    def notify(self, state, module):
        module.notify(state)