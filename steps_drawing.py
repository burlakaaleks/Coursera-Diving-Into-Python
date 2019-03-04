import sys

num_steps = int(sys.argv[1])

# num_steps = 20
spaces = 0
brackets = 0

for i in range(1, num_steps + 1):
    spaces = num_steps - i
    brackets = num_steps - spaces
    print(' ' * spaces + '#' * brackets)
