import time

lines = []
with open("test.txt", "r") as file:
    for line in file:
        lines.append(line.strip())
ranges = []

for line in lines:
    if line == "":
        break
    ranges.append((int(line.split("-")[0]), int(line.split("-")[1])))
idx = lines.index("")+1
ids = [int(id) for id in lines[idx:]]  
freshCount = 0

# #Approach 1: Naive version -> Hangs with Large_test_input.txt
# start = time.time()
# for id in ids:
#     isFresh = True
#     for r in ranges:
#         if r[0] <= id <= r[1]:
#             freshCount += 1
#             break
# end = time.time()
# print("Approach 1 answer: ", freshCount)
# print(end - start, "seconds for Approach 1")

# print()
# print()

# freshCount = 0

# #Optimized version
# start = time.time()
# order = []
# for r in ranges:
#     order.append((r[0], "start"))
#     order.append((r[1], "end"))
# for id in ids:
#     order.append((id, "id"))
# order.sort(key = lambda x: (x[0], 0 if x[1] == "start" else 1 if x[1] == "id" else 2))
# active  = 0

# for item in order:
#     if item[1] == "start":
#         active += 1
#     elif item[1] == "end":
#         active -= 1
#     else: # id
#         if active > 0:
#             freshCount += 1

# end = time.time()
# print("Approach 2 answer: ", freshCount)
# print(end - start, "seconds for Approach 2")

def merge_intervals(intervals):
    # Sort the intervals based on the starting point
    intervals.sort(key=lambda x: x[0])
    merged = []
    for current in intervals:
        if not merged or merged[-1][1] < current[0]:
            merged.append(current)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], current[1]))
    return merged

# Approach 3, using binary searcg
freshCount = 0
#ranges = merge_intervals(ranges)
#ranges.sort(key=lambda x: (x[0], x[1]))  # Ensure ranges are sorted for binary search
ranges.sort()


def binary_search(id): # returns True if id is in any range
    l=0
    r=len(ranges)-1
    while l <= r:
        range_mid = (l+r)//2
        left,right = ranges[range_mid]
        if left <= id <= right:
            return True
        elif id < left:
            r = range_mid - 1
        else:
            l = range_mid + 1
    return False

missing = []
for id in ids:
    if binary_search(id):
        freshCount += 1
        
print("Approach 3 answer: ", freshCount)
print("Missing IDs: ", missing)
