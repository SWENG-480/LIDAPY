from abc import ABC, abstractmethod


class AgentFactory(ABC):

    """
    Creates and returns a {@link Agent} from specified {@link Properties}
	 @param agent_type
	        Agent properties
	 @return Constructed {@link Agent} object
    """

    @abstractmethod
    def get_agent(self, agent_type):
        pass

    @abstractmethod
    def add_module(self, module_name, module_instance):
        pass

    def get_module(self, module_name):
        pass