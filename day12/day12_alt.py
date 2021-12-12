# Day 12: Passage Pathing

from collections import Counter
import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

class Path:
  def __init__(self, nodes=None):
    if nodes is None:
      self.list = []
      self.set = set()
    else:
      self.list = [x for x in nodes]
      self.set = set(self.list)
    self.has_repeated = False
  def tail(self):
    return self.list[-1]
  def add(self, node):
    if node in self.set:
      self.has_repeated = True
    self.list.append(node)      
    self.set.add(node)
  def __contains__(self, node):
    return node in self.set
  def copy(self):
    new_path = Path(self.list)
    new_path.has_repeated = self.has_repeated
    return new_path

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
stack.append(Path(["start"]))
while len(stack) > 0:
  path = stack.pop()
  tail = path.tail()
  if tail == "end":
    paths.append(path)
    continue
  for child in adjacent[tail]:
    if child.isupper() or child not in path:
      new_path = path.copy()
      new_path.add(child)
      stack.append(new_path)

print("Part 1:", len(paths))

# ------------------------------------------------------------------------------
# Part 2

paths = []
stack = []
stack.append(Path(["start"]))
while len(stack) > 0:
  path = stack.pop()
  tail = path.tail()
  if tail == "end":
    paths.append(path)
    continue
  for child in adjacent[tail]:
    if child == "start":
      continue
    elif child.isupper() or child not in path or not path.has_repeated:
      new_path = path.copy()
      new_path.add(child)
      stack.append(new_path)

print("Part 2:", len(paths))
