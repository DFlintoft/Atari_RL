import numpy as np
import gym
from gym import spaces


class MoonLander(gym.Env):
    def __init__(self):
        super(MoonLander, self).__init__()
        self.env = gym.make("LunarLander-v2", render_mode="human")

    def step(self, action: int):
        pass

    def reset(self):
        self.env.reset()
