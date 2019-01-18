""" A simple Q-learning agent. Maintains an action-value matrix while exploring
the gridworld. """

import random

class RlAgent:

  def __init__(self,
           num_actions,
           num_states,
           epsilon=0.2, 
           epsilon_decay=100,
           discount_factor=0.9):
    """
    Args:
      num_actions: The number of available actions
      num_states: The number of possible game states
      epsilon: Final epsilon value while training
      epsilon_decay: Epsilon will decay by a factor of ten every epsilon_decay iterations
      discout_factor: Discount factor for calculating return based on future rewards
    """
    self._num_actions = num_actions
    self._num_states = num_states
    self._epsilon = epsilon
    self._epsilon_decay = epsilon_decay
    self._discount_factor = discount_factor
    
  def _choose_action(self, state):
    """Chooses an action based on the current state"""
    return input("Choose action (0-3)")

  def begin_episode(self, state):
    """Begins a new training episode"""
    return self._choose_action(state)

  def end_episode(self, state):
    """Marks the end of a training episode"""
    pass

  def step(self, reward, state):
    """Performs a single step. Updates Action-Value matrix then returns the 
    next action
    """
    return self._choose_action(state)

