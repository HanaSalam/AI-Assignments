"""
4. Render any  3 environments in OpenAi gym.
"""

import gym
import numpy as np
env = gym.make("FrozenLake-v0")
state = env.reset()
#env.env.s=0
env.render()


Q = np.zeros([16,4])
count = 1
reward = 0

print 'obs: ',env.observation_space
print 'action: ',env.action_space

state,reward,done,action = env.step(0)
env.render()
print state,reward,done,action

for episode in range(1,1000):
    state = env.reset()
    #env.render()
    count = 1
    reward = 0
    gamma = 0.8
    done=False
    while reward!=1:
        if done==True:
          break
        action = np.argmax(Q[state])
        state2,reward,done,info = env.step(action)
        Q[state,action] = reward+gamma*np.max(Q[state2])
        state = state2
        count+=1
    if episode%50==0:
        print(str(count)+' moves needed to reach final state for episode '+str(episode))


