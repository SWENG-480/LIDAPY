#LIDA Cognitive Framework
#Pennsylvania State University, Course : SWENG480
#Authors: Katie Killian, Brian Wachira, and Nicole Vadillo

#from Environment import Environment as env

"""
This module can temporarily store sensory data from the environment and then
process and transfer to further working memory.
"""
from src.Framework.Agents.AgentAdapter import AgentAdapter
from src.ModuleObserver.ModuleNotifier import ModuleNotifier


class SensoryMotorMemoryImpl:
    def __init__(self, environment, agent):
        self.listeners = [] #initializing an empty list to store the listeners
        self.action = None  # store selected_action reference
        self.environment = environment
        self.agent = agent
        self.observer = AgentAdapter()
        self.notifier = ModuleNotifier()
        self.notifier.add_observer(self.observer)
        self.state = None
        self.reward = None
        self.done = None
        self.truncated = None
        self.info = None
        self.surrounding_tiles = None
        #self.motor_plan = motor_plan # reference to the motor_plan that will be executed

    def add_sensory_listener(self, listener):
        """Adding the listener to the memory"""
        self.listeners.append(listener) #appending the listener to the list

    def notify(self, state, percept, action):
        """The selected action from action selection"""
        #Logic to gather information from the environment
        #Example: Reading the current state or rewards
        self.state = state
        self.action = action
        self.send_action_execution_command(action, percept)
        '''
        #state, info = self.environment.reset() # use environment instance to reset
        #percept = self.pam.retrieve_associations(state) # retrieve percept from PAM
        #return state, percept # get state and percept from environment instance
        #return state, info # get state and info from environment instance
        '''
        #return state, reward, done, truncated, info


    def send_action_execution_command(self, action_plan, percept):
        """
        Returning the content from this Sensory Motor Memory
        :param action_plan: Specifying the action(s) to take
        :return: content corresponding to the action_plan
        """
        if percept == "danger":
            print(f"\nPercept: {percept}!..Rerouting")
            self.observer.notify_(self.state, self.agent, self.reward,
                                  self.done, self.truncated,
            self.info, action_plan,self.surrounding_tiles)
        else:
            #Logic to retrieve and return data based on the modality.
            print(f"\nPercept: {percept}..")
            self.environment.step(action_plan, self.agent)