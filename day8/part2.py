from collections import defaultdict
lines = []
with open("test.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

coordinates_str = [line.split(',') for line in lines]
coordinates = []
for x,y,z in coordinates_str:
    x = int(x)
    y = int(y)
    z = int(z)
    coordinates.append((x,y,z))

count_pairs = 10 # pairs to find

def compute_pairwise():
    pair = ()
    min_distance = float('inf')
    res = []
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            x1, y1, z1 = coordinates[i]
            x2, y2, z2 = coordinates[j]
            distance = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
            res.append((coordinates[i], coordinates[j], distance))
    return res


parent = []
size=[]
i = 0
mapping = {}
for coord in coordinates:
    mapping[(coord)] = i
    parent.append(i)
    size.append(1)
    i += 1

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        parent[rootY] = rootX
        size[rootX] += size[rootY]
        size[rootY] = 0

pairwise_distances = compute_pairwise()
pairwise_distances.sort(key=lambda x: x[2]) # Sort by distance

count_pairs = 10
remaining = len(size)
ans= []
while remaining > 1:
    point1, point2 = pairwise_distances.pop(0)[:2]
    
    idx1 = mapping[point1]
    idx2 = mapping[point2]
    #print(point1, idx1, point2, idx2)
    #print(find(idx1), find(idx2))
    
    if find(idx1) != find(idx2):
        if remaining == 2:
            # here we are connecting the last two circuits
            ans.append(point1)
            ans.append(point2)
        # New Connection. less circuits remainig
        remaining -= 1
        union(idx1, idx2)

    count_pairs -= 1
size.sort()
print(point1[0]*point2[0])