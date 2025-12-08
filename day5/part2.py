lines = []
with open("test.txt", "r") as file:
    for line in file:
        lines.append(line.strip())
ranges = []

for line in lines:
    if line == "":
        break
    ranges.append([int(line.split("-")[0]), int(line.split("-")[1])])
idx = lines.index("")+1
ids = [int(id) for id in lines[idx:]]  

# merge intervals, then just count
# 16 18 18 20, merge when end >= nextStart
# 10 45 16 25
#  10 20 30 40

ranges.sort()
merged = []
for s,e in ranges:
    if not merged or merged[-1][-1] < s:
        merged.append([s,e])
    else:
        
        merged[-1][-1] =  max(merged[-1][1], e)

fresh=0
for s,e in merged:
    fresh += (e - s + 1)
print(fresh)


