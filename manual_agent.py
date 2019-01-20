""" A simple Q-learning agent. Maintains an action-value matrix while exploring
the gridworld. """

import random

class ManualAgent:

  def __init__(self, num_actions):
    """
    Args:
      num_actions: The number of available actions
    """
    self._num_actions = num_actions
    
  def _choose_action(self, state):
    """Prompts the user to pick an action"""
    return int(input("Choose action (0-{})".format(self._num_actions - 1)))

  def begin_episode(self, state):
    """Begins a new training episode"""
    return self._choose_action(state)

  def end_episode(self, state):
    """Marks the end of a training episode"""
    pass

  def step(self, reward, state):
    """Performs a single step."""
    return self._choose_action(state)

