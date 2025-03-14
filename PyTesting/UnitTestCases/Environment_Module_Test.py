import pytest
from src.Environment.FrozenLakeEnvironment import FrozenLakeEnvironment
from gymnasium import make


@pytest.fixture
def env():
    """
    Pytest fixture to initialize the FrozenLake environment before each test.
    Ensures a fresh instance is used for every test function.
    """
    environment = FrozenLakeEnvironment(render_mode="rgb_array", size=4)
    yield environment  # Provides the environment instance to test functions
    environment.close()  # Cleanup after test execution


def test_reset_function(env):
    """
    Tests that the reset function properly initializes the environment
    and places the agent in the correct starting position.
    """
    state, info, surrounding_tiles, col, row = env.reset(module="test_module")

    # Assertions to verify the correct initial state
    assert col == 0, "Agent should start at column 0"
    assert row == 0, "Agent should start at row 0"
    assert isinstance(surrounding_tiles, dict), "Surrounding tiles should be a dictionary"
    assert state is not None, "State should not be None after reset"


def test_step_function(env):
    """
    Tests the step function by moving the agent in the Frozen Lake environment
    and verifying state updates.
    """
    initial_col, initial_row = env.get_attribute("col"), env.get_attribute("row")

    new_state, reward, done, truncated, info = env.step(action=1, module="test_module")  # Move down

    # Verifying if the agent's position has updated correctly
    assert env.get_attribute("row") == initial_row + 1, "Row should increase when moving down"

    # Ensuring reward and done flag are correctly returned
    assert isinstance(reward, float), "Reward should be a floating point number"
    assert isinstance(done, bool), "Done should be a boolean indicating episode completion"


def test_render_function(env):
    """
    Tests the render function to ensure it does not raise any errors.
    """
    try:
        env.render()
    except Exception as e:
        pytest.fail(f"Render function raised an error: {e}")


def test_update_position_function(env):
    """
    Tests the update_position function to check if the agent moves correctly
    based on the action taken.
    """
    env.update_position(action=2)  # Move right
    assert env.get_attribute("col") == 1, "Column should increase when moving right"

    env.update_position(action=0)  # Move left
    assert env.get_attribute("col") == 0, "Column should return to original position"


def test_update_position_boundaries(env):
    """
    Tests update_position function for boundary conditions.
    Ensures the agent does not move out of bounds.
    """
    env.update_position(action=3)  # Attempt to move up at the top boundary
    assert env.get_attribute("row") == 0, "Agent should not move above row 0"

    env.update_position(action=0)  # Attempt to move left at the left boundary
    assert env.get_attribute("col") == 0, "Agent should not move left of column 0"