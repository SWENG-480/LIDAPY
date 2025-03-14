from unittest.mock import Mock

import pytest
from src.PAM.PAM import PerceptualAssociativeMemory

@pytest.fixture
def pam_setup():
    """
    Fixture to initialize the Perceptual Associative Memory (PAM) system.
    Mocks dependencies for isolated testing.
    """
    procedural_memory_mock = MagicMock()
    pam = PerceptualAssociativeMemory(procedural_memory=procedural_memory_mock)
    return pam, procedural_memory_mock


def test_add_association(pam_setup):
    """
    Test the add_association method.
    Verifies that associations are correctly added to the PAM.
    """
    pam, _ = pam_setup

    # Add an association
    cue = "Move up, Current state: 1"
    pattern = "goal"
    pam.add_association(cue, pattern)

    # Assert the association is stored correctly
    assert pattern in pam.associations
    assert cue in pam.associations[pattern]


def test_retrieve_association_existing(pam_setup):
    """
    Test the retrieve_associations method for an existing cue.
    Ensures it retrieves the correct association.
    """
    pam, _ = pam_setup

    # Add an association first
    cue = "Move left, Current state: 2"
    pattern = "danger"
    pam.add_association(cue, pattern)

    # Retrieve the association
    retrieved = pam.retrieve_associations(cue)

    # Assert that the retrieved association is correct
    assert retrieved == pam.associations[pattern]


def test_retrieve_association_non_existing(pam_setup):
    """
    Test the retrieve_associations method for a non-existing cue.
    Ensures it creates a default association.
    """
    pam, _ = pam_setup

    cue = "Move right, Current state: 3"
    retrieved = pam.retrieve_associations(cue)

    # Assert default association is created
    assert "default-pattern-{cue}" in retrieved


def test_notify(pam_setup):
    """
    Test the notify method.
    Verifies that it triggers correct updates and calls the procedural memory module.
    """
    pam, procedural_memory_mock = pam_setup

    # Mock event
    event = {
        "state": 1,
        "surrounding_tiles": ["S", "H", "G"],
        "action": "Move up"
    }

    # Notify PAM
    pam.notify(event)

    # Assert attributes are updated correctly
    assert pam.get_attribute("state") == event["state"]
    assert pam.get_attribute("surrounding_tiles") == event["surrounding_tiles"]
    assert pam.get_attribute("action") == event["action"]

    # Assert procedural memory is notified
    procedural_memory_mock.notify.assert_called_once()


def test_learn(pam_setup):
    """
    Test the learn method.
    Validates that the correct associations are created based on the input state and outcome.
    """
    pam, _ = pam_setup

    # Set up mock action_value and surrounding tiles
    pam.add_attribute("action_value", {"3": "up", "2": "right", "1": "down", "0": "left"})
    state = 1
    outcome = {"up": "G", "down": "H"}
    action = 3

    # Call learn
    pam.learn(state, outcome, action)

    # Verify that associations are added correctly
    cue = "Move up, Current state: 1"
    pattern = "goal"
    assert cue in pam.associations[pattern]


def test_get_position(pam_setup):
    """
    Test the get_position method.
    Validates that the position is calculated correctly based on the state.
    """
    pam, _ = pam_setup

    # Test for various state values
    assert pam.get_position(2) == [0, 2]
    assert pam.get_position(6) == [1, 2]
    assert pam.get_position(10) == [2, 2]
    assert pam.get_position(14) == [3, 2]