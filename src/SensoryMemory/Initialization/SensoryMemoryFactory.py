from abc import ABC, abstractmethod

class SensoryMemoryFactory(ABC):
    """
    Creates and returns a SensoryMemoryModule
    """
    @abstractmethod
    def create_sensory_memory(self, sensory_memory):
        pass
    @abstractmethod
    def add_attribute(self, attribute, value):
        pass
    @abstractmethod
    def update_attribute(self, attribute_name, value):
        pass
    @abstractmethod
    def get_attribute(self, attribute_name):
        pass

    @abstractmethod
    def add_module(self, module_name, module_instance):
        pass

    @abstractmethod
    def get_module(self, module_name):
        pass

    @abstractmethod
    def run_sensors(self, state=None, col=None, row=None, agent=None):
        pass