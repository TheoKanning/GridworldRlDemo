# GridworldRlDemo
A Reinforcement Learning demo using a simple gridworld agent. Shows concepts like reward, Q-function, and the Bellman equation without using neural networks.

## How to run
`python train.py`

To use the manual agent:
`python train.py --manual`

## environment.py
This script controls the state of the Gridworld game.
Just like a typical reinforcement learning environment, it takes in an action and returns a reward and a new state.

## runner.py
Controls looping through training steps and connects the agent to the environment.

## rl_agent.py
A Q-learning agent that explores the environment. 
After each step, it updates its internal Q matrix with its latest action value estimates.
Each estimate is equal to its immediate reward plus the value of the best action in the next state.

## manual_agent.py
An agent that chooses actions by prompting for keyboard commands. Up=0, Down=1, Left=2, Right=3
