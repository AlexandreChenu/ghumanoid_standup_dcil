import os
import gym
from gym.envs.registration import register

__version__ = "0.1.0"


def envpath():
    resdir = os.path.join(os.path.dirname(__file__))
    return resdir


print("gym-ghumanoid: ")
print("|    gym version and path:", gym.__version__, gym.__path__)

print("|    REGISTERING GHumanoid-v0 from", envpath())
register(
    id="GHumanoid-v0",
    entry_point="gym_ghumanoid.envs:GHumanoid",
)

print("|    REGISTERING GHumanoidGoal-v0 from", envpath())
register(
    id="GHumanoidGoal-v0",
    entry_point="gym_ghumanoid.envs:GHumanoidGoal",
)

# print("|    REGISTERING GFetchDCIL-v0 from", envpath())
# register(
#     id="GFetchDCIL-v0",
#     entry_point="gym_gfetch.envs:GFetchDCIL",
#     reward_threshold=1.,
# )
