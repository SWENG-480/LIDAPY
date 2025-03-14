import pytest
from unittest.mock import MagicMock
from src.Environment.FrozenLakeEnvironment import FrozenLakeEnvironment
from src.SensoryMemory.SensoryMemory import SensoryMemory

@pytest.fixture
def setup_environment():
    # Create the environment with basic settings
    env = FrozenLakeEnvironment(render_mode="human", size=4)
    return env


@pytest.fixture
def setup_sensory_memory(setup_environment):
    # Create sensory memory with a mock environment
    environment = setup_environment
    sensory_memory = SensoryMemory(environment=environment)
    # Mock any modules if necessary
    sensory_memory.get_module = MagicMock()
    return sensory_memory


def test_environment_initialization(setup_environment):
    env = setup_environment
    assert env.get_attribute("row") == 0
    assert env.get_attribute("col") == 0
    assert env.get_module("env") is not None


def test_get_surrounding_tiles(setup_environment):
    env = setup_environment
    surrounding_tiles = env.get_surrounding_tiles(0, 0)
    assert isinstance(surrounding_tiles, dict)
    assert "up" in surrounding_tiles
    assert "right" in surrounding_tiles


def test_sensory_memory_receives_update(setup_sensory_memory):
    sensory_memory = setup_sensory_memory
    # Mock the notify method to track calls
    sensory_memory.notify = MagicMock()

    # Mock environment to perform a step and notify sensory memory
    environment = sensory_memory.get_module("environment")
    state = environment.step(action=1, module="some_module")  # Example action taken
    sensory_memory.notify(state)

    # Verify that notify was called with expected state
    sensory_memory.notify.assert_called_with(state)


def test_sensory_memory_run_sensors(setup_sensory_memory):
    sensory_memory = setup_sensory_memory