import gym
import numpy as np

env = gym.make("Taxi-v3").env
env.reset()
q_table = np.zeros([env.observation_space.n, env.action_space.n])


"""Evaluate agent's performance after Q-learning"""

total_epochs, total_penalties = 0, 0
episodes = 100

for _ in range(episodes):
    state = env.reset()
    epochs, penalties, reward = 0, 0, 0

    done = False

    while not done:
        action = np.argmax(q_table[state])
        state, reward, done, info = env.step(action)

        if reward == -10:
            penalties += 1

        epochs += 1

    total_penalties += penalties
    total_epochs += epochs

print(f"Results after {episodes} episodes:")
print(f"Average timesteps per episode: {total_epochs / episodes}")
print(f"Average penalties per episode: {total_penalties / episodes}")

# Results after 100 episodes:
# Average timesteps per episode: 12.3
# Average penalties per episode: 0.0

# We can see from the evaluation,
# the agent's performance improved significantly and it incurred no penalties,
# which means it performed the correct pickup/dropoff actions with 100 different passengers.

# We evaluate our agents according to the following metrics,

# Average number of penalties per episode
# Average number of timesteps per trip
# Average rewards per move
