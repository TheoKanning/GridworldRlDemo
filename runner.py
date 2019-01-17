"""Reinforcement learning  experiment runner. This class connecst the agent
and environment by passing actions, states, and rewards back and for for a set
number of iterations.
"""

import agent

class Runner:

  def __init__(self,
	       agent,
	       num_iterations=10000,
	       log_every_n=1,
	       max_steps_per_episode=100):
    """Args:
         agent: The agent to train
         num_iterations: Total number of training iterations
         log_every_n: Log training progress every n iterations
         max_steps_per_episode: Stop an episode after this many iterations
    """
    self._agent = agent
    self._num_iterations=num_iterations
    self._log_every_n=log_every_n
    self._max_steps_per_episode=max_steps_per_episode

  def run_experiment(self):
    pass

  def _run_one_episode(self):
    """Runs an entire episode to termination. Stops when agent reaches terminal
       state or exceeds step limit
    """
    pass

  def _run_one_step(self):
    """Runs a single game step by getting the agent's action, passing it to the
       environemt, then updating the agent with the new reward and observation
    """ 
    pass

  def _initialize_episode(self):
    """Starts an episode by resetting the environment and updating the agent""" 
    pass

  def _end_episode(self):
    """Notifies the agent that the episode has ended"""
    pass
