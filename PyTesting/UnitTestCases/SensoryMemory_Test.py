import pytest
from unittest.mock import Mock
from src.SensoryMemory.SensoryMemory import SensoryMemory


@pytest.fixture
def setup_sensory_memory():
    # Create mock objects for environment, pam, and agent
    environment = Mock()
    pam = Mock()
    agent = Mock()

    # Initialize sensory memory with mock objects
    sensory_memory = SensoryMemory(environment=environment, pam=pam, agent=agent)

    return sensory_memory, environment, pam, agent


def test_run_sensors(setup_sensory_memory):
    sensory_memory, environment, pam, agent = setup_sensory_memory

    # Set up the environment mock
    environment.reset.return_value = ("state", "info", "surrounding_tiles", "col", "row")
    environment.get_attribute.side_effect = lambda x: {"col": "col", "row": "row", "action_space": Mock()}.get(x)
    environment.get_surrounding_tiles.return_value = "surrounding_tiles"

    # Run the function
    sensory_memory.run_sensors()

    # Verify behavior
    environment.reset.assert_called_once()
    environment.get_attribute.assert_any_call("col")
    environment.get_attribute.assert_any_call("row")
    environment.get_surrounding_tiles.assert_called_once()


def test_notify(setup_sensory_memory):
    sensory_memory, environment, pam, agent = setup_sensory_memory

    # Test notify method with a state
    test_state = "new_state"
    sensory_memory.notify(test_state)

    # Verify state is updated correctly
    assert sensory_memory.get_attribute("state") == test_state


def test_get_sensory_content(setup_sensory_memory):
    sensory_memory, environment, pam, agent = setup_sensory_memory

    # Mock PAM learn method
    pam.learn = Mock()

    # Call get_sensory_content
    state = "state_data"
    outcome = "outcome_data"
    result = sensory_memory.get_sensory_content(state, outcome, modality="visual", params={"key": "value"})

    # Check if pam.learn was called correctly
    pam.learn.assert_called_once_with(state, outcome)
