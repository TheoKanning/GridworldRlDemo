import argparse
import manual_agent, rl_agent
import environment
import runner

parser = argparse.ArgumentParser("Train Gridworld Agent")
parser.add_argument('--manual', nargs='?', type=bool, help='Use this flag to control the agent manually', const=True, default=False)
args = parser.parse_args()

if __name__ == '__main__':
  if args.manual:
    agent = manual_agent.ManualAgent(4)
  else:
    agent = rl_agent.RlAgent(4, 9, learning_rate=1)

  environment = environment.Gridworld()
  runner = runner.Runner(agent, environment, num_iterations=1000)

  runner.run_experiment()
