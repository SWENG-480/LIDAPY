from src.SensoryMemory.Initialization.SensoryMemoryFactory import \
    SensoryMemoryFactory

class ConcreteSensoryMemoryFactory(SensoryMemoryFactory):
    def __init__(self):
        super().__init__()
        self.attributes = {}
        self.modules = {}

    def add_attribute(self, attribute, value):
        self.attributes[attribute] = value

    def update_attribute(self, attribute_name, value):
        self.attributes[attribute_name] = value

    def get_attribute(self, attribute_name):
        return self.attributes[attribute_name]

    def add_module(self, module_name, module_instance):
        self.modules[module_name] = module_instance

    def get_module(self, module_name):
        return self.modules[module_name]

    def run_sensors(self, state=None, col=None, row=None, agent=None):
        pass

