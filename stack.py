
def push(stack,val):
  stack.append(15)

def main():
  stack = range(10)
  print stack
  push(stack, 25)
  print stack

if __name__ == '__main__':
  main()