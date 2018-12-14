"""
1. Using the Taxi environment in Open AI , reset the environments and display some states  of your choice.
2. Starting with a state of your choice, manualy pickup a passenger and drop the passenger at his desired location.
down-0,up-1,right=2,left=3,pickup=4,dropoff5
"""
import gym
env = gym.make("Taxi-v2")
state = env.reset()


env.env.s=348
env.render()


print('Possible states: ',str(env.observation_space.n))
print('Possible actions: ',str(env.action_space.n))


state,reward,done,action = env.step(1)
env.render()
print state,reward,done,action

state,reward,done,action = env.step(3)
env.render()
print state,reward,done,action


state,reward,done,action = env.step(3)
env.render()
print state,reward,done,action


state,reward,done,action = env.step(0)
env.render()
print state,reward,done,action

state,reward,done,action = env.step(0)
env.render()
print state,reward,done,action


state,reward,done,action = env.step(4)
env.render()
print state,reward,done,action

state,reward,done,action = env.step(1)
env.render()
print state,reward,done,action
state,reward,done,action = env.step(1)
env.render()
print state,reward,done,action
state,reward,done,action = env.step(1)
env.render()
print state,reward,done,action
state,reward,done,action = env.step(1)
env.render()
print state,reward,done,action
state,reward,done,action = env.step(5)
env.render()
print state,reward,done,action

