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

for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == '@':
            if check(i,j,mat):
                rolls += 1  
print(rolls)