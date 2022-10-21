from environment import MoonLander
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.env_util import make_atari_env, make_vec_env
from stable_baselines3.ppo.ppo import PPO
from stable_baselines3.dqn import DQN

env = MoonLander()
print(env.env.action_space)
print(env.env.observation_space)