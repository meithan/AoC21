# Day 12: Passage Pathing

from collections import Counter
import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
adjacent = {}
with open(sys.argv[1]) as f:
  for line in f:
    name1, name2 = line.strip().split("-")
    if name1 not in adjacent:
      adjacent[name1] = set()
    if name2 not in adjacent:
      adjacent[name2] = set()
    adjacent[name1].add(name2)
    adjacent[name2].add(name1)

for name, children in adjacent.items():
  print(name, children)

# ------------------------------------------------------------------------------
# Part 1

paths = []
stack = []
stack.append(["start"])
while len(stack) > 0:
  path = stack.pop()
  node = path[-1]
  if node == "end":
    paths.append(path)
    continue
  for child in adjacent[node]:
    if child.isupper() or child not in path:
      new_path = path + [child]
      stack.append(new_path)

print("Part 1:", len(paths))

# ------------------------------------------------------------------------------
# Part 2

paths = []
stack = []
stack.append(["start"])
while len(stack) > 0:
  path = stack.pop()
  node = path[-1]
  if node == "end":
    paths.append(path)
    continue
  for child in adjacent[node]:
    if child == "start":
      continue
    elif child.isupper():
      new_path = path + [child]
      stack.append(new_path)
    elif child not in path:
      new_path = path + [child]
      stack.append(new_path)
    else:
      has_twice = False
      seen = set()
      for n in path:
        if n.islower():
          if n in seen:
            has_twice = True
            break
          else:
            seen.add(n)
      if not has_twice:
        new_path = path + [child]
        stack.append(new_path)

print("Part 2:", len(paths))
