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
        #self.procedural_memory.add_scheme("safe", 2)
        #self.procedural_memory.add_scheme("danger", 0)

        '''
        # state rules for 4x4 map
        self.procedural_memory.add_scheme("state-0", 2)  # move right
        self.procedural_memory.add_scheme("state-1", 2)  # move right
        self.procedural_memory.add_scheme("state-2", 1)  # move down
        self.procedural_memory.add_scheme("state-6", 1)  # move down
        self.procedural_memory.add_scheme("state-9", 2)  # move right
        self.procedural_memory.add_scheme("state-10", 2)  # move right
        self.procedural_memory.add_scheme("state-14", 3)  # move up
        self.procedural_memory.add_scheme("goal", None) # finish when goal reached
        '''

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

        #Agents behavior logic
        self.state, self.action, surrounding_tiles, col, row, = \
            (sensory_memory.run_sensors(self.state, None, None, self))
        print(f"Initial Observation: State: {self.state}, Percept: {surrounding_tiles}")

        while not self.done:
            if self.state is None:
                # Use environment instance to reset
                state, info, surrounding_tiles, col, row = self.env.reset(self)
            else:
                col, row = self.env.col, self.env.row
                # Agents behavior logic
                sensory_memory.run_sensors(self.state, col, row, self)

            #self.action = self.env.action_space.sample()
            #step_result = self.env.step(action, self)
            #state, reward, done, truncated, info, surrounding_tiles = step_result
            print(f"Action: {self.action}\n")
            print(f"State: {self.state}, Reward: {self.reward}, Done: {self.done}, Info: {self.info}")
            print(f"Surrounding Tiles: {surrounding_tiles}")


            #state, reward, done, truncated, info = self.env.step(action)
            #self.env.render()

            #surrounding_tiles = self.env.get_surrounding_tiles(self.env.row, self.env.col)

            '''
            state_str = "state-"
            state_id_str = state_id.__str__()
            state_str += state_id_str
            
            if state == 15:         # goal state in 4x4 map
                self.pam.learn(state_str, "goal")
            elif reward == 0 and done: # fell into a hole
                self.pam.learn(state_str, "hole")
                print(f"Action: {action}\n")
            else: # safe state
                self.pam.learn(state_str, "safe")

            action = env.action_space.sample() #Take a random actio
            self.procedural_memory.add_scheme(state_str, action)
            percept = self.pam.retrieve_associations(state_str)  # update percept
            '''
        env.close()

