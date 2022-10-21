from environment import MoonLander
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.env_util import make_atari_env, make_vec_env
from stable_baselines3.ppo.ppo import PPO
from stable_baselines3.dqn import DQN

import gym

env = gym.make("LunarLander-v2", render_mode="human")

print(env.observation_space)
