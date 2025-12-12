from collections import defaultdict
lines = []
with open("test.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

points = []
for line in lines:
    p1,p2 = line.split(',')
    points.append((int(p1), int(p2)))

n = len(points)
maxArea = 0
for i in range(n):
    for j in range(i+1, n):
        p1, p2 = points[i], points[j]
        area = abs(p1[0]-p2[0]+1) * abs(p1[1]-p2[1]+1)
        maxArea = max(maxArea, area)

