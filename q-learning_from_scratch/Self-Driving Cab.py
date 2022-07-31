# There are 4 locations (labeled by different letters), and our job is to pick up the passenger at one location and drop him off at another.
# We receive +20 points for a successful drop-off and lose 1 point for every time-step it takes.
# There is also a 10 point penalty for illegal pick-up and drop-off actions.

import gym

env = gym.make("Taxi-v3").env
env.reset()
# env.render()

print("Action Space {}".format(env.action_space))
print("State Space {}".format(env.observation_space))

state = env.encode(
    3, 1, 2, 0
)  # (taxi row, taxi column, passenger index, destination index)
print("State:", state)

env.s = state
# env.render()

# {action: [(probability, nextstate, reward, done)]}
env.P[328]

# The 0-5 corresponds to the actions (south, north, east, west, pickup, dropoff)
# the taxi can perform at our current state in the illustration.


