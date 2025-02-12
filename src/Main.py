#LIDA Cognitive Framework
#Pennsylvania State University, Course : SWENG480
#Authors: Katie Killian, Brian Wachira, and Nicole Vadillo

from src.ActionSelection.ActionSelection import ActionSelection
from src.Environment.Environment import FrozenLakeEnvironment
from src.Framework.Agents.Agent import Agent
from src.Framework.Initialization.ConcreteAgentFactory import ConcreteAgentFactory
from src.PAM.PAM import PerceptualAssociativeMemory
from src.ProceduralMemory.ProceduralMemory import ProceduralMemory
from src.SensoryMemory.SensoryMemory import SensoryMemory
from src.SensoryMotorMemory.SensoryMotorMemoryImpl import \
    SensoryMotorMemoryImpl


if __name__ == "__main__":
    # create factory and initialize agent
    factory = ConcreteAgentFactory()
    agent = factory.get_agent(Agent())

    #Add the environment module to the agent
    agent.add_module("FrozenLakeEnvironment", FrozenLakeEnvironment())

    #Add Sensory Motor Memory module
    agent.add_module("SensoryMotorMemoryImpl",
                     SensoryMotorMemoryImpl(
                         agent.get_module("FrozenLakeEnvironment"), agent))

    # Add the Action Selection Module
    agent.add_module("ActionSelection", ActionSelection(
        agent.get_module("FrozenLakeEnvironment"),
        agent.get_module("SensoryMotorMemoryImpl")))

    # Add Procedural Memory
    agent.add_module("ProceduralMemory", ProceduralMemory(
        agent.get_module("ActionSelection")))

    # Add PAM
    agent.add_module("PerceptualAssociativeMemory",
                     PerceptualAssociativeMemory(
                         agent.get_module("ProceduralMemory")))

    #Add the Sensory Memory module
    agent.add_module("SensoryMemory",
                     SensoryMemory(agent.get_module(
                         "FrozenLakeEnvironment"),
                     agent.get_module("PerceptualAssociativeMemory"),agent))

    #Add attributes relevant to this agent
    agent.add_attribute("state", None)
    agent.add_attribute("action", None)
    agent.add_attribute("reward", None)
    agent.add_attribute("done", False)
    agent.add_attribute("info", None)
    agent.add_attribute("truncated", False)
    agent.add_attribute("surrounding_tiles", None)
    agent.add_attribute("col", None)
    agent.add_attribute("row", None)

    #Start the agent
    agent.run()