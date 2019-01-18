"""This class represents a python Gridworld environment. Actions sent to this
class will update the state of the environment and return a reward"""

AGENT='A'
OPEN=' '
OBSTACLE='#'
GOAL='G'

ACTIONS=[
          (0, -1), # up
          (0, 1),  # down
          (-1, 0), # left
          (1, 0)   # right
        ]

class Gridworld:

  def __init__(self,
               step_reward=-0.25,
               obstacle_reward=-2,
               goal_reward=10):
    """Args:
         step_reward: The reward for taking a single step in the Gridworld
         obstacle_reward: The reward for running into an obstacle
         goal_reward: The final reward for completing the world
    """

    self._step_reward = step_reward
    self._obstacle_reward = obstacle_reward
    self._goal_reward = goal_reward
    self._height = 3
    self._width = 3
    self._agentX = 0
    self._agentY = 2
    self._environment = [[OPEN, OPEN, GOAL],
                         [OBSTACLE, OPEN, OBSTACLE],
                         [OPEN, OPEN, OPEN]]

  def step(self, action):
    """Performs the given action and returns a reward, updated state, and a 
       boolean indicating if the state is terminal. State is return as a single
       integer corresponding to the agent's current cell number, starting in
       the top left

    """
    (self._agentX, self._agentY) = self._get_agent_destination(action)
    reward = self._get_reward(self._agentX, self._agentY) + self._step_reward
    terminal = self._environment[self._agentY][self._agentX] == GOAL
    state = self._agentY * self._width + self._agentX
 
    return (reward, state, terminal)

  def reset(self):
    """Completely resets the Gridworld"""
    pass

  def log(self):
    """Logs the current Gridworld state"""
    rowDivider = " _"*self._width
    print rowDivider

    for row in range(self._height): 
      rowString = "|"
      for cell in range(self._width):
        if row == self._agentY and cell == self._agentX:
	  rowString += AGENT
        else:
          rowString += self._environment[row][cell]
        rowString += "|"
      print rowString

  def _get_agent_destination(self, action):
    """Takes an action and determines the agent's new position"""

    def clamp(number, lower, upper):
      return max(min(number, upper), lower)

    delta = ACTIONS[action]
    newX = clamp(self._agentX + delta[0], 0, self._width - 1)
    newY = clamp(self._agentY + delta[1], 0, self._height - 1)

    return (newX, newY)

  def _get_reward(self, x, y):
    """Returns the reward at the given position"""
    cell = self._environment[y][x]
    if cell == OPEN:
      return 0
    elif cell == OBSTACLE:
      return self._obstacle_reward
    elif cell == GOAL:
      return self._goal_reward
    else:
      print "Unknown reward for cell = {} at ({},{})".format(cell, x, y)
      return 0
