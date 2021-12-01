# Day 1: Sonar Sweep

import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Read (and possibly pre-process) input
depths = []
with open(sys.argv[1]) as f:
  for line in f:
    depths.append(int(line.strip()))

# ------------------------------------------------------------------------------
# Part 1

count = 0
for i in range(1, len(depths)):
 if depths[i] > depths[i-1]:
   count +=1

ans1 = count
print("Part 1:", ans1)

# ------------------------------------------------------------------------------
# Part 2

count2 = 0
last_sum = None
for i in range(2,len(depths)):
  cur_sum = depths[i] + depths[i-1] + depths[i-2]
  if last_sum is not None and cur_sum > last_sum:
    count2 += 1
  last_sum = cur_sum

ans2 = count2
print("Part 2:", ans2)
