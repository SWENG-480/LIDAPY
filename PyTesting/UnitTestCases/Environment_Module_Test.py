import pytest
from src.Environment.FrozenLakeEnvironment import FrozenLakeEnvironment
from gymnasium import make

@pytest.fixture #Decorator
def environment():
    return FrozenLakeEnvironment()

"""Testing the rest function"""
def test_reset(environment, mocker):
    module_mock = mocker.Mock()
    state, info, surrounding_tiles, col, row = environment.reset(module_mock)

    assert col == 0
    assert row == 0
    assert state is not None
    assert info is not None
    mocker.spy(environment, 'get_surrounding_tiles')
    environment.get_surrounding_tiles.assert_called_once_with(0,0)

def test_step(environment, mocker):
    action = 2 #Example action of the agent moving right
    module_mock = mocker.Mock()

    mocker.spy(environment, 'update_position')
    state, reward, done, truncated, info = environment.step(action, module_mock)

    environment.update_position.assert_called_once_with(action)
    assert state is not None
    assert reward is not None
    assert done is not None
    assert truncated is not None
    assert info is not None

def test_render(environment, mocker):
    mocker.patch.object(environment.get_module("env"), 'render')
    environment.render()
    environment.get_module("env").render.assert_called_once_with()

def test_update_position(environment):
    environment.update_position(2) #move right
    assert environment.get_attribute("col") == 1
    assert environment.get_attribute("row") == 0

    environment.update_position(1) # moving down
    assert environment.get_attribute("row") == 1

    environment.update_position(0) #move left
    assert environment.get_attribute("col") == 0

    environment.update_position(3) #move up
    assert environment.get_attribute("row") == 0
