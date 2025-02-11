#LIDA Cognitive Framework
#Pennsylvania State University, Course : SWENG480
#Authors: Katie Killian, Brian Wachira, and Nicole Vadillo
from src.ModuleObserver.ModuleNotifier import ModuleNotifier
from src.SensoryMotorMemory.SensoryMotorAdapter import SensoryMotorAdapter
from src.SensoryMotorMemory.SensoryMotorMemoryImpl import \
    SensoryMotorMemoryImpl


class ActionSelection:
    def __init__(self, environment, sensory_motor):
        self.scheme = None
        self.environment = environment
        self.sensory_motor = sensory_motor
        self.observer = SensoryMotorAdapter()
        self.notifier = ModuleNotifier()
        self.state = None
        self.notifier.add_observer(self.observer)

    def select_action(self, percept, action, module):
        self.observer.notify_(self.state, module, percept, action)

    def notify(self, scheme):
        self.scheme = scheme
        self.state = scheme["State"]
        self.select_action(scheme["Percept"], scheme["Action"],
                           self.sensory_motor)


















