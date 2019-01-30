""" A simple Q-learning agent. Maintains an action-value matrix while exploring
the gridworld. """

import random
import numpy as np

class RlAgent:

  def __init__(self,
           num_actions,
           num_states,
           learning_rate=1,
           epsilon=0.5):
    """
    Args:
      num_actions: The number of available actions
      num_states: The number of possible game states
      learning_rate: The rate at which the Q function is updated with new rewards
      epsilon: Chance of taking a random action
    """
    self._num_actions = num_actions
    self._num_states = num_states
    self._learning_rate = learning_rate
    self._epsilon = epsilon
    self._q_function = np.zeros((num_states, num_actions))
    self._last_action = 0
    self._last_state = 0

  def _choose_action(self, state):
    """Chooses the next action using an epsilon-greedy scheme. If a randomly
    selected number is greater than epsilon, choose the action with the highest
    expected return. Otherwise, pick a random action"""
    if random.random() > self._epsilon:
      # pick the action with the highest expected return for the given state
      return np.argmax(self._q_function[state])
    else:
      # return random action
      return random.randint(0, self._num_actions - 1)

  def begin_episode(self, state):
    """Begins a new training episode"""
    self._last_state = state
    action = self._choose_action(state)
    self._last_action = action
    return action

  def end_episode(self, reward):
    """Marks the end of a training episode. Updates the q function without
    taking into account future discounted rewards"""
    old_q_value = self._q_function[self._last_state][self._last_action]
    learned_value = reward # don't add term for future states since we're done
    new_q_value = (1 - self._learning_rate) * old_q_value + self._learning_rate * learned_value
    self._q_function[self._last_state][self._last_action] = new_q_value

  def step(self, reward, state):
    """Performs a single step. Updates Action-Value matrix then returns the 
    next action
    """
    self._update_q_function(state, reward)
    self._last_state = state
    action = self._choose_action(state)
    self._last_action = action
    print(self._q_function)
    return action

  def _update_q_function(self, new_state, reward):
    """Updates the Q function using the state transition and reward. The new Q value
    is a combination of the old value and the new learned value based on the reward
    for the previous action and the estimated return from the new state"""
    old_q_value = self._q_function[self._last_state][self._last_action]
    learned_value = reward + np.max(self._q_function[new_state])
    new_q_value = (1 - self._learning_rate) * old_q_value + self._learning_rate * learned_value
    self._q_function[self._last_state][self._last_action] = new_q_value

