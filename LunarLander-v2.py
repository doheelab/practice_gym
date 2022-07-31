import gym

if __name__ == "__main__":

    env = gym.make("LunarLander-v2")  #
    env.action_space.seed(42)

    observation, info = env.reset(seed=42, return_info=True)

    for _ in range(1000):
        # env.render()
        observation, reward, done, info = env.step(env.action_space.sample())

        if done:
            observation, info = env.reset(return_info=True)

    env.close()


# the format of valid actions
env.action_space

# the format of valid observations is specified by
env.observation_space

# we sampled random actions via
env.action_space.sample()
