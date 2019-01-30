"""Reinforcement learning  experiment runner. This class connecst the agent
and environment by passing actions, states, and rewards back and for for a set
number of iterations.
"""

class Runner:

  def __init__(self,
	       agent,
               environment,
               num_iterations=100):
    """Args:
         agent: The agent to train
         environment: Environment in which to train the agent
         num_iterations: Total number of training steps. Each step is a single
           gridworld action.
    """
    self._agent = agent
    self._environment = environment
    self._iteration = 0
    self._num_iterations=num_iterations

  def run_experiment(self):
    while self._iteration < self._num_iterations:
      self._run_one_episode()

  def _run_one_episode(self):
    """Runs an entire episode to termination. Stops when agent reaches terminal
       state or exceeds step limit
    """
    action = self._initialize_episode()
    episode_reward = 0

    while True:
      self._iteration += 1
      (reward, state, terminated) = self._environment.step(action)
      episode_reward += reward
      self._environment.log()
      print("Reward:{} Terminated:{}".format(reward, terminated))

      if terminated:
        self._agent.end_episode(reward)
        print("Episode complete, total score={}".format(episode_reward))
        break

      action = self._agent.step(reward, state)

  def _initialize_episode(self):
    """Starts an episode by resetting the environment. Returns agent's first
      action """
    state = self._environment.reset()
    self._environment.log()
    return self._agent.begin_episode(state)

