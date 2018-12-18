"""
3. Implement the Q Learning Algorith on the Taxi environment.

"""

import gym
import numpy as np
env = gym.make("Taxi-v2")
Q = np.zeros([500,6])


for episode in range(1,1000):
    state = env.reset()
    #env.render()
    count = 1
    reward = 0
    gamma = 0.8 
    while reward!=20:
        action = np.argmax(Q[state])
        state2,reward,done,info = env.step(action)
        Q[state,action] = reward+gamma*np.max(Q[state2])
        state = state2
        count+=1
    if episode%50==0:
        print(str(count)+' moves needed to reach final state for episode '+str(episode))
