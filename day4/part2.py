from collections import deque
lines = []
with open("test.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

mat = [[e for e in line] for line in lines ]

# just check all eight directions for each roll
def check(i,j,mat):
    directions = [(1,0), (0,1), (1,1), (1,-1), (-1,0), (0,-1), (-1,-1), (-1,1)]
    count = 0
    for di,dj in directions:
        ni = i + di
        nj = j + dj
        if 0 <= ni < len(mat) and 0 <= nj < len(mat[0]) and mat[ni][nj] == '@':
            count += 1
        
        
    return count < 4

rolls = 0

# loop through each roll
q = deque([])
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == '@':
            if check(i,j,mat):
                q.append((i,j))  
# Queue holds all rolls to be removed
# When we remove all the rolls, check all the neighbors of those to see if they also removed

print(q)
while q:
    n = len(q)
    possible = []
    for _ in range(n):
        i,j = q.popleft()
        if mat[i][j] == '@':
            mat[i][j] = '.'
            rolls += 1
            directions = [(1,0), (0,1), (1,1), (1,-1), (-1,0), (0,-1), (-1,-1), (-1,1)]
            for di,dj in directions:
                ni = i + di
                nj = j + dj
                if 0 <= ni < len(mat) and 0 <= nj < len(mat[0]) and mat[ni][nj] == '@':
                    # dont hceck here because theres 
                    # #other rolls to remove in this level check after we removed all roles for this level
                    possible.append((ni,nj))
    for i,j in possible:
        if check(i,j,mat):
            q.append((i,j))
print(rolls)
# changes = True 
# rolls = 0
# while True:
#     changes = False
#     for i in range(len(mat)):
#         for j in range(len(mat[0])):
#             if mat[i][j] == '@':
#                 if check(i,j,mat):
#                     rolls += 1
#                     changes = True
#                     mat[i][j] = '.'
#     if not changes:
#         break
# print(rolls)