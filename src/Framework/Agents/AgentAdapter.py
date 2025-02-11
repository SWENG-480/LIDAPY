from src.ModuleObserver.ModuleObserver import ModuleObserver


class AgentAdapter(ModuleObserver):
    def __init__(self):
        super().__init__()

    def notify(self, state, module):
        pass

    def notify_(self, state, module, reward, done, truncated, info, action,
                surrounding_tiles):
        module.notify(state, reward, done, truncated, info, action,
                      surrounding_tiles)