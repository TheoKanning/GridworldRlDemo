"""This class represents a python Gridworld environment. Actions sent to this
class will update the state of the environment and return a reward"""

class Girdworld:

  def __init__(self,
               step_cost=0.25,
               obstacle_cost=2,
               reward=10):
    """Args:
         step_cost: The cost of taking a single step in the Gridworld
         obstacle_cost: The cost of running into an obstacle
         reward: The final reward for completing the world
    """

    self._environment = []
    self._step_cost = step_cost
    self._obstacle_cost = obstacle_cost
    self._reward = reward

  def step(self, action):
    """Performs the given action and returns a reward, updated state, and a 
       boolean indicating if the state is terminal
    """
    pass

  def reset(self):
    """Completely resets the Gridworld"""
    pass

  def log(self):
    """Logs the current Gridworld state"""
    pass
