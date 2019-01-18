import agent
import environment
import runner

if __name__ == '__main__':
  agent = agent.RlAgent(4, 9)
  environment = environment.Gridworld()
  runner = runner.Runner(agent, environment)

  runner.run_experiment()
