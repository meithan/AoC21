# Day 03: Binary Diagnostic

import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Read (and possibly pre-process) input
numbers = []
with open(sys.argv[1]) as f:
  for line in f:
    numbers.append(line.strip())

# ------------------------------------------------------------------------------
# Part 1

N = len(numbers)
S = len(numbers[0])

gamma = []
epsilon = []
for i in range(S):
  count0s = count1s = 0
  for num in numbers:
    if num[i] == "1":
      count1s += 1
    else:
      count0s += 1
  if count1s > count0s:
    gamma.append("1")
    epsilon.append("0")
  else:
    gamma.append("0")
    epsilon.append("1")

gamma = int("".join(gamma), 2)
epsilon = gamma ^ (2**S-1)

ans1 = gamma * epsilon
print("Part 1:", ans1)

# ------------------------------------------------------------------------------
# Part 2

remain = [x for x in numbers]
s = 0
while len(remain) > 1:
  new_remain = []
  count1s = 0
  count0s = 0
  for num in remain:
    if num[s] == "1":
      count1s += 1
    else:
      count0s += 1
  most_freq = "1" if count1s >= count0s else "0"
  for num in remain:
    if num[s] == most_freq:
      new_remain.append(num)
  remain = new_remain
  s += 1
oxy = int(remain[0], 2)

remain = [x for x in numbers]
s = 0
while len(remain) > 1:
  new_remain = []
  count1s = 0
  count0s = 0
  for num in remain:
    if num[s] == "1":
      count1s += 1
    else:
      count0s += 1
  least_freq = "1" if count1s < count0s else "0"
  for num in remain:
    if num[s] == least_freq:
      new_remain.append(num)
  remain = new_remain
  s += 1
CO2 = int(remain[0], 2)

ans2 = oxy * CO2
print("Part 2:", ans2)
