import pytest
from src.ProceduralMemory.ProceduralMemory import ProceduralMemory

def test_add_scheme():
    procedural_memory = ProceduralMemory()
    percept = "goal"
    action = "move_forward"

    # Add a scheme
    procedural_memory.add_scheme(percept, action)

    # Assert that the scheme is stored correctly
    assert procedural_memory.schemes[percept] == action

def test_get_action():
    procedural_memory = ProceduralMemory()
    percept = "danger"
    action = "move_backward"

    # Add a scheme
    procedural_memory.add_scheme(percept, action)

    # Fetch the action for a given percept
    retrieved_action = procedural_memory.get_action(percept)

    # Assert that the retrieved action matches the expected action
    assert retrieved_action == action

    # Test for a percept that does not exist
    assert procedural_memory.get_action("unknown") is None

def test_notify(mocker):
    procedural_memory = ProceduralMemory()
    percept_data = {"Percept": "safe", "Action": "halt"}

    # Mock the notify function of ActionSelectionAdapter
    mock_notify = mocker.patch('ActionSelectionAdapter.notify')

    # Call notify
    procedural_memory.notify(percept_data)

    # Assert that the percept attribute was updated correctly
    assert procedural_memory.get_attribute("percept") == percept_data["Percept"]

    # Assert that the scheme was added correctly
    assert procedural_memory.schemes[percept_data["Percept"]] == percept_data["Action"]

    # Verify that the notify method of ActionSelectionAdapter was called correctly
    mock_notify.assert_called_once_with(percept_data, procedural_memory.get_module("action_selection"))