import gym
from gym.envs.registration import register

from .taxi import *
from .windy_cliff_walking import *
from .frozen_lake import *

__all__ = ['TaxiEnv', 'RewardingFrozenLakeEnv', 'WindyCliffWalkingEnv']

register(
    id='Taxi-v0',
    entry_point='environments:TaxiEnv',
)

register(
    id='RewardingFrozenLake-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '4x4'},
)

register(
    id='RewardingFrozenLake8x8-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '8x8'}
)

register(
    id='RewardingFrozenLakeNoRewards20x20-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '20x20', 'rewarding': False}
)

register(
    id='RewardingFrozenLakeNoRewards8x8-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '8x8', 'rewarding': False}
)

register(
    id='CliffWalking4x4-v0',
    entry_point='environments:WindyCliffWalkingEnv',
    kwargs={'map_name': '4x4', 'wind_prob': 0.0}
)


register(
    id='CliffWalking4x12-v0',
    entry_point='environments:WindyCliffWalkingEnv',
    kwargs={'map_name': '4x12', 'wind_prob': 0.0}
)


register(
    id='CliffWalking6x12-v0',
    entry_point='environments:WindyCliffWalkingEnv',
    kwargs={'map_name': '6x12', 'wind_prob': 0.0}
)


register(
    id='WindyCliffWalking4x4-v0',
    entry_point='environments:WindyCliffWalkingEnv',
    kwargs={'map_name': '4x4', 'wind_prob': 0.1}
)


register(
    id='WindyCliffWalking4x12-v0',
    entry_point='environments:WindyCliffWalkingEnv',
    kwargs={'map_name': '4x12', 'wind_prob': 0.1}
)


register(
    id='WindyCliffWalking6x12-v0',
    entry_point='environments:WindyCliffWalkingEnv',
    kwargs={'map_name': '6x12', 'wind_prob': 0.1}
)

def get_small_taxi():
    return gym.make('Taxi-v0')


def get_rewarding_frozen_lake_environment():
    return gym.make('RewardingFrozenLake8x8-v0')


def get_frozen_lake_environment():
    return gym.make('FrozenLake-v0')


def get_rewarding_no_reward_frozen_lake_environment():
    return gym.make('RewardingFrozenLakeNoRewards8x8-v0')


def get_large_rewarding_no_reward_frozen_lake_environment():
    return gym.make('RewardingFrozenLakeNoRewards20x20-v0')


def get_cliff_walking_environment():
    return gym.make('CliffWalking-v0')


def get_small_cliff_walking_environment():
    return gym.make('CliffWalking4x4-v0')


def get_medium_cliff_walking_environment():
    return gym.make('CliffWalking4x12-v0')


def get_large_cliff_walking_environment():
    return gym.make('CliffWalking6x12-v0')


def get_small_windy_cliff_walking_environment():
    return gym.make('WindyCliffWalking4x4-v0')


def get_medium_windy_cliff_walking_environment():
    return gym.make('WindyCliffWalking4x12-v0')


def get_large_windy_cliff_walking_environment():
    return gym.make('WindyCliffWalking6x12-v0')