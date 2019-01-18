import environment

if __name__ == '__main__':
  environment = environment.Gridworld()
  environment.log()

  while(True):
    action = input("Enter an action (0-3)")
    environment.step(action)
    environment.log()
