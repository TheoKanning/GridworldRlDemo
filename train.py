import manual_agent
import environment
import runner

if __name__ == '__main__':
  agent = manual_agent.ManualAgent(4)
  environment = environment.Gridworld()
  runner = runner.Runner(agent, environment)

  runner.run_experiment()
