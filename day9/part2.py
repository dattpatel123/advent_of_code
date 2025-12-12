
from collections import defaultdict
from functools import cache
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
edges = []
borders= set()


for (x1,y1),(x2,y2) in zip(points, points[1:] + [points[0]]):
    edges.append(((x1,y1),(x2,y2)))
    if x1 == x2:
        for y in range(min(y1,y2), max(y1,y2)+1):
            borders.add((x1,y))
    if y1 == y2:
        for x in range(min(x1,x2), max(x1,x2)+1):
            borders.add((x,y1))


@cache
def is_inside(xp,yp):
    count = 0 
    if (xp,yp) in borders:
        return True
    for (x1,y1),(x2,y2) in edges:
        if ((y1 > yp) != (y2 > yp)) and (xp < x1 + ((yp-y1)/(y2-y1))*(x2-x1)):
            count += 1
    return count % 2 == 1
#print(edges)

def valid(x1,y1,x2,y2, ex1,ey1,ex2,ey2):
    if ex1 == ex2:
        if not(x1 < x2 <= ex1 or ex1 <= x1 < x2): # Overlap vertical
            if not (y1 >= ey2 or y1 <= ey1):
                return False
            
                
    # Horizontal edge
    if ey1 == ey2:
        if not(y1 < y2 <= ey1 or ey1 <= y1 < y2):
            if not (x1 >= ex2 or x1 <= ex1):
                return False
    return True

def within_bounds(x1,y1,x2,y2):
    # go trhrough all edges, make sure the edge is either fully within polygon
    x1,y1 = min(x1,x2), min(y1,y2)
    x2,y2 = max(x1,x2), max(y1,y2)
    x3,y3 = x1,y2
    x4,y4 = x2,y1

    for (ex1,ey1),(ex2,ey2) in edges:
        ex1,ex2 = min(ex1,ex2), max(ex1,ex2)
        ey1,ey2 = min(ey1,ey2), max(ey1,ey2)
        # If edge goes out of bounds
        # Verical edge
        if not valid(x1, y1, x2,y2, ex1,ey1,ex2,ey2):
            return False
        # if not valid(x1, y1, x4,y4, ex1,ey1,ex2,ey2):
        #     return False
        # if not valid(x3, y3, x2,y2, ex1,ey1,ex2,ey2):
        #     return False
        # if not valid(x3, y3, x4,y4, ex1,ey1,ex2,ey2):
        #     return False

    return True

maxArea = 0

for i in range(n):
    for j in range(i+1, n):
        print(i,j)
        (x1,y1) = points[i]
        (x2,y2) = points[j]
        x1,x2 = min(x1,x2), max(x1,x2)
        y1,y2 = min(y1,y2), max(y1,y2)
        area = (x2 - x1 + 1) * (y2 - y1 + 1)
        if area <= maxArea:
            continue
        if within_bounds(x1,y1,x2,y2) and is_inside(x1,y1) and is_inside(x2,y2) and is_inside(x1,y2) and is_inside(x2,y1):
            
            print(area, (x1,y1), (x2,y2))
            maxArea = max(maxArea, area)
print(maxArea)

