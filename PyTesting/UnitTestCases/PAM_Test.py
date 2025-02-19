from unittest.mock import Mock

import pytest
from src.PAM.PAM import PerceptualAssociativeMemory

@pytest.fixture
def pam_instance():
    # Mock or initialize necessary components like procedural_memory
    procedural_memory = Mock()  # You would replace Mock with the actual object or a meaningful mock
    return PerceptualAssociativeMemory(procedural_memory)

def test_add_association(pam_instance):
    cue = "sample_cue"
    pattern = "sample_pattern"
    pam_instance.add_association(cue, pattern)
    assert cue in pam_instance.associations[pattern]

def test_retrieve_associations_existing(pam_instance):
    cue = "sample_cue"
    pattern = "sample_pattern"
    pam_instance.add_association(cue, pattern)
    retrieved = pam_instance.retrieve_associations(cue)
    assert retrieved == [cue]

def test_retrieve_associations_non_existing(pam_instance):
    cue = "new_cue"
    pattern = pam_instance.retrieve_associations(cue)
    assert "default-pattern-new_cue" in pam_instance.associations
    assert pattern == ["new_cue"]

def test_notify(pam_instance):
    event = {
        "state": 3,
        "surrounding_tiles": None,
        "action": 2
    }
    pam_instance.notify(event)
    assert pam_instance.get_attribute("state") == 3
    assert pam_instance.get_attribute("action") == 2

def test_get_position(pam_instance):
    position = pam_instance.get_position(2)
    assert position == [0, 2]
    position = pam_instance.get_position(5)
    assert position == [1, 2]
    position = pam_instance.get_position(10)
    assert position == [2, 3]
    position = pam_instance.get_position(15)
    assert position == [3, 4]

def test_learn_goal(pam_instance):
    state = 1
    outcome = {"up": "G"}
    action = 3
    pam_instance.learn(state, outcome, action)