from src.Framework.Initialization.AgentFactory import AgentFactory


class ConcreteAgentFactory(AgentFactory):
# concrete factory for creating and initializing agents
    def __init__(self):
        super().__init__()
        self.modules = {}
        self.attributes = {}

    def get_agent(self, agent_type):
        return agent_type

    def add_module(self, module_name, module_instance):
        # add a module to the agent
        self.modules[module_name] = module_instance

    def get_module(self, module_name):
        return self.modules.get(module_name)  # retrieve a module by name

    def add_attribute(self, attribute, value):
        self.attributes[attribute] = value

    def update_attribute(self, attribute_name, value):
        self.attributes[attribute_name] = value

    def get_attribute(self, attribute_name):
        return self.attributes.get(attribute_name)