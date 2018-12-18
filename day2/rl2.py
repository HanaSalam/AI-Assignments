"""
1. Using the Taxi environment in Open AI , reset the environment.
2. Using random moves pickup a passenger and drop the passenger at his desired location. Find out how many moves had to 
"""

import gym
env = gym.make("Taxi-v2")
state = env.reset()
env.render()

count = 1
reward = 0
while reward!=20:
    action = env.action_space.sample()
    state,reward,done,info = env.step(action)
    env.render()
    count+=1

print(str(count)+" moves required to reach final state.")
