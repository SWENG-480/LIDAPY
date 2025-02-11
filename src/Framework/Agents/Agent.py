#LIDA Cognitive Framework
#Pennsylvania State University, Course : SWENG480
#Authors: Katie Killian, Brian Wachira, and Nicole Vadillo

from src.ActionSelection.ActionSelection import ActionSelection
from src.PAM.PAM import PerceptualAssociativeMemory
from src.SensoryMemory.SensoryMemory import SensoryMemory
from src.Environment.Environment import FrozenLakeEnvironment
from src.ProceduralMemory.ProceduralMemory import ProceduralMemory
from src.SensoryMotorMemory.SensoryMotorMemoryImpl import SensoryMotorMemoryImpl


class Agent:
    def __init__(self):
        self.env =  FrozenLakeEnvironment()
        self.sensory_motor_memory = SensoryMotorMemoryImpl(self.env, self)

        # pass in procedural memory
        self.action_selection = ActionSelection(self.env,
                                                self.sensory_motor_memory)
        # initialize procedural memory
        self.procedural_memory = ProceduralMemory(self.action_selection)

        # create pam instance
        self.pam = PerceptualAssociativeMemory(self.procedural_memory)

        # pass in environment and pam instance
        self.sensory_memory = SensoryMemory(self.env, self.pam,
                                            self)
        self.modules = {}
        self.state = None
        self.action = None
        self.reward = None
        self.done = False
        self.info = None
        self.truncated = False
        self.surrounding_tiles = None
        self.col = None
        self.row = None

    def add_module(self, module_name, module_instance):
        self.modules[module_name] = module_instance  # add a module to the agent

    def get_module(self, module_name):
        return self.modules.get(module_name)  # retrieve a module by name

    def notify(self, state, reward, done, truncated , info, action,
               surrounding_tiles):
         self.state = state
         self.reward = reward
         self.done = done
         self.truncated = truncated,
         self.info = info,
         self.action = action
         self.surrounding_tiles = surrounding_tiles
    def run(self):
        env = self.get_module("Environment")
        action_selection = self.get_module("ActionSelection")
        sensory_memory = self.get_module("SensoryMemory")
        procedural_memory = self.get_module("ProceduralMemory")
        sensory_motor_memory = self.get_module("SensoryMotorMemory")

        # Agents behavior logic
        while not self.done:
            if self.state is None:
                sensory_memory.run_sensors(self.state, None, None, self)
                print(
                    f"Initial Observation: State: {self.state}, "
                    f"Percept: {self.surrounding_tiles}")
            else:
                self.col, self.row = self.env.col, self.env.row
                sensory_memory.run_sensors(self.state, self.col, self.row, self)

            print(f"Action: {self.action}\n")
            print(f"State: {self.state}, Reward: {self.reward}, "
                  f"Done: {self.done}, Info: {self.info}")
            print(f"Surrounding Tiles: {self.surrounding_tiles}")

        env.close()

