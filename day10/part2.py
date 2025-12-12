from collections import defaultdict, deque
from functools import cache
from z3 import *

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
    joltTuple = tuple([int(x) for x in jolts[1:-1].split(',')])
    
    machines.append([diag, buttons, joltTuple])


# # def findMinimumStepsForMachine(machine):
        

# #     # BFS holds my states
    
# #     machineWiring = machine[1]
# #     endState = machine[2]
# #     n = len(endState)
# #     startState = tuple(0 for _ in range(n))
# #     print(startState, endState)
    
# #     q = deque([startState])
# #     visited = set()
# #     visited.add(startState)
# #     steps = -1
# #     while q:
# #         size = len(q)
# #         steps += 1

# #         for _ in range(size):
            
# #             state = q.popleft()
# #             if state == endState:
# #                 return steps
# #             # try each posible state of button flips
# #             for wiring in machineWiring:
# #                 possible = list(state)
# #                 for button in wiring:
                    
# #                     possible[button] += 1
                    
                        
# #                 newState = tuple(possible)
# #                 if newState in visited:
# #                     continue
# #                 visited.add(newState)
# #                 q.append(newState)
# #     #print(steps)

# #     return steps

# def findMinimumStepsForMachine(machine):
        

#     # BFS holds my states
    
#     machineWiring = machine[1]
#     endState = machine[2]
#     n = len(endState)
#     startState = tuple(0 for _ in range(n))
#     print(startState, endState)
    
#     q = deque([startState])
#     visited = set()
#     visited.add(startState)
    
#     @cache
#     def dfs(state):
#         #curPath = curPath + [state]
#         #print(curPath)
#         if state == endState:
#             return 0
#         min_steps = float('inf')
#         for wiring in machineWiring:
#             possible = list(state)
#             for button in wiring:
                
#                 possible[button] += 1
#             valid = True
#             # invalid state
#             for i in range(n):
#                 if possible[i] > endState[i]:
#                     valid = False
#                     break
            
#             if not valid:
#                 continue
#             newState = tuple(possible)
#             if newState in visited:
#                 continue
#             visited.add(newState)
#             min_steps = min(dfs(newState) + 1, min_steps)
#             visited.remove(newState)
#         return min_steps
            
            
            
#     return dfs(startState)


def findMinimumStepsForMachine(machine):
    coefficients = []
    machineWiring = machine[1]
    joltageReq = machine[2]
    n = len(joltageReq)
    
    for counterIndex in range(n):
        coeff = [0 for _ in range(len(machineWiring))]

        for buttonIdx in range(len(machineWiring)):
            if counterIndex in machineWiring[buttonIdx]:
                coeff[buttonIdx] = 1
                continue
        coefficients.append(coeff)
    import numpy as np
    
    
    A = np.array(coefficients)
    b = np.array(list(joltageReq))
    

    num_vars = A.shape[1]
    vars = [Int(f'x{i}') for i in range(num_vars)]
    s = z3.Optimize()
    for i in range(A.shape[0]):
        eq = s.add(sum([A[i][j] * vars[j] for j in range(num_vars)]) == b[i])
    #print(s.check(), s.model())
    
    for v in vars:
        s.add(v >= 0)
    
    solution=[]
    s.minimize(sum(vars))
    if s.check() == z3.sat:
        m = s.model()
        solution = [m[v].as_long() for v in vars]  # get integer values
        print("Solution:", solution)
    else:
        print("No solution")
        
    
    return sum(solution)     



        
            

total = 0

for machine in machines:
    #print(machine)
    total += findMinimumStepsForMachine(machine)
    
    
    
    
print(total)

            