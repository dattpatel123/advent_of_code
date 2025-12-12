from collections import defaultdict, deque
from functools import cache
lines = []
with open("test.txt", "r") as file:
    for line in file:
        lines.append(line.strip())
machines = []
for line in lines:
    parts = line.split(' ')
    diag = parts[0]
    jolts = parts[-1]
    buttons = [tuple((int(x),)) if ',' not in x else tuple(map(int, x.split(',')))
    for x in (p.strip('()') for p in parts[1:-1])
    ]
    machines.append([diag, buttons])

def findMinimumStepsForMachine(machine):
        

    # BFS holds my states
    
    machineWiring = machine[1]
    endState = tuple(machine[0][1:-1])
    n = len(endState)
    startState = tuple('.' for _ in range(n))
    
    q = deque([startState])
    visited = set()
    visited.add(startState)
    steps = -1
    while q:
        size = len(q)
        steps += 1

        for _ in range(size):
            
            state = q.popleft()
            if state == endState:
                return steps
            # try each posible state of button flips
            for wiring in machineWiring:
                possible = list(state)
                for button in wiring:
                    if possible[button] == '.':
                        possible[button] = '#'
                    else:
                        possible[button] = '.'
                newState = tuple(possible)
                if newState in visited:
                    continue
                visited.add(newState)
                q.append(newState)
    print(steps)

    return steps

total = 0
for machine in machines:
    total += findMinimumStepsForMachine(machine)
print(total)

            