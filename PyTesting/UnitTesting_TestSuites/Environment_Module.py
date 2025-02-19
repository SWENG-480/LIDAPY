import pytest
from gymnasium import make
from src.Environment.FrozenLakeEnvironment import FrozenLakeEnvironment

@pytest.fixture
def env():
    """A fixture to create the fozen lake environment"""
    environment = FrozenLakeEnvironment()
    yield environment
    environment.close()

def test_initialize_environment(env):
    """Testing to ensure that the environment initializes properly"""
    assert env is not None
    #Checking of the environment is GYM
    assert hasattr(env.get_module("env"), 'reset')
    initial_state, info = env.reset(module = None)
    assert initial_state is not None
    assert 'surrounding_tiles' in env.__dict__

def test_rest_environment(env):
    """Testing the rest functionality of the environment"""
    initial_state, info = env.reset(module = None)
    assert initial_state is not None
    assert env.col == 0
    assert env.row == 0
    assert isinstance(env.get_surrounding_tiles(env.row, env.col), dict)

def test_environment_configuration():
    """Testing the configuration of the environment"""
    env = make('FrozenLake-v1', is_slippery=False)
    assert env is not None
    initial_state, _ = env.reset()
    assert initial_state is not None
    step_data = env.step(env.action_space.sample()) #taking a random action
    assert len(step_data) == 5 #state, reward, done, truncated, info

if __name__ == '__main__':
    pytest.main([__file__])