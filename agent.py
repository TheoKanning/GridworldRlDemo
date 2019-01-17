""" A simple Q-learning agent. Maintains an action-value matrix while exploring
the gridworld. """


class RlAgent:

  def __init__(self, 
           epsilon=0.2, 
           epsilon_decay=100,
           discount_factor=0.9):
    """
    Args:
      epsilon: Final epsilon value while training
      epsilon_decay: Epsilon will decay by a factor of ten every epsilon_decay iterations
      discout_factor: Discount factor for calculating return based on future rewards
    """
    self._epsilon = epsilon
    self._epsilon_decay = epsilon_decay
    self._discount_factor = discount_factor
    
  def _choose_action(self, state):
    """Chooses an action based on the current state"""
    pass

  def begin_episode(self, state):
    """Begins a new training episode"""
    pass

  def end_episode(self, state):
    """Marks the end of a training episode"""
    pass

  def step(self, reward, observation):
    """Performs a single step. Updates Action-Value matrix then returns the 
    next action
    """
    return self._choose_action(state)

