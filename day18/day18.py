# Day 18: Snailfish

from math import ceil, floor
import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
lines = []
with open(sys.argv[1]) as f:
  for line in f:
    lines.append(line.strip())

# ------------------------------------------------------------------------------

def add(a, b):
  return Node(a,b)

class Node:

  def __init__(self, left, right, parent=None):
    if type(left) == list:
      self.left = Node(left[0], left[1], self)
    else:
      self.left = left
    if type(right) == list:
      self.right = Node(right[0], right[1], self)
    else:
      self.right = right
    self.parent = parent

  def find_nested(self):

    level = 1
    node = self
    while True:
      if level == 4:
        if type(node.left) is Node or type(node.right) is Node:
          return node
        else:
          return None
      elif type(node.left) is Node:
        node = node.left
        level += 1
      elif type(node.right) is Node:
        node = node.right
        level += 1
      else:
        print(level)
        break
    return None


  def reduce(self):

    while True:

      # Find and explode first 4-nested pair
      pair = self.find_nested()
      if pair is not None:
        if type(pair.left) == Node:
          node = pair.parent
          while node is not None:
            if type(node.left) is int:
              node.left += pair.left.left
            node = node.parent
          pair.right += pair.left.right
          pair.left = 0
        elif type(pair.right) == Node:
          node = pair.parent
          while node is not None:
            if type(node.right) is int:
              node.right += pair.right.right
            node = node.parent
          pair.left += pair.right.left
          pair.right = 0
        continue

      # Split regular number
      # if bla bla
      #   continue

      break

  def __repr__(self):
    l = repr(self.left) if type(self.left) is Node else str(self.left)
    r = repr(self.right) if type(self.right) is Node else str(self.right)
    return f"[{l},{r}]"

# ------------------------------------------------------------------------------

def find_number(pair, i0, dir):
  if dir == 1:
    i = i0+1
    while i < len(pair):
      if pair[i].isnumeric():
        j = i
        while j < len(pair):
          if not pair[j].isnumeric():
            return i, j-1
          j += 1
      i += 1
  elif dir == -1:
    j = i0-1
    while j >= 0:
      if pair[j].isnumeric():
        i = j-1
        while i >= 0:
          if not pair[i].isnumeric():
            return i+1, j
          i -= 1
      j -= 1
  return None

def explode(pair):

  # Find first 5-nested pair
  level = 0
  for i in range(len(pair)):

    if pair[i] == "[":
      level += 1
    elif pair[i] == "]":
      level -= 1

    if level == 5 and pair[i] == "[":
      j1 = i
      # find closing ]
      k = i+1
      while True:
        if pair[k] == "]":
          j2 = k
          break
        k += 1
      # extract numbers
      a, b = (int(x) for x in pair[j1+1:j2].split(","))
      # find previous number (if any)
      left = find_number(pair, j1-1, -1)
      if left is not None:
        k1, k2 = left
        n1 = int(pair[k1:k2+1])
      # find next number (if any)
      right = find_number(pair, j2+1, +1)
      if right is not None:
        l1, l2 = right
        n2 = int(pair[l1:l2+1])
      # build new pair
      if left is not None:
        new_pair = pair[:k1] + str(a+n1) + pair[k2+1:j1]
      else:
        new_pair = pair[:j1]
      new_pair += "0"
      if right is not None:
        new_pair += pair[j2+1:l1] + str(b+n2) + pair[l2+1:]
      else:
        new_pair += pair[j2+1:]

      # print("Exploded pair", pair[j1:j2+1])
      return new_pair

  return None

def split(pair):

  i0 = 0
  while True:
    result = find_number(pair, i0, +1)
    if result is None:
      return None
    else:
      i, j = result
      n = int(pair[i:j+1])
      if n > 9:
        a = int(floor(n/2))
        b = int(ceil(n/2))
        new_pair = pair[:i] + f"[{a},{b}]" + pair[j+1:]
        # print("Split number", pair[i:j+1])
        return new_pair
      else:
        i0 = j+1

def reduce(pair):

  while True:

    # print(pair)

    # Try to explode a subpair
    new_pair = explode(pair)
    if new_pair is not None:
      pair = new_pair
      continue

    # Try to split a number
    new_pair = split(pair)
    if new_pair is not None:
      pair = new_pair
      continue

    break

  return pair

def add(pair1, pair2):
  return f"[{pair1},{pair2}]"

def parts(pair):
  level = 0
  for i in range(len(pair)):
    if pair[i] == "[":
      level += 1
    elif pair[i] == "]":
      level -= 1
    elif pair[i] == "," and level == 1:
      break
  left = pair[1:i]
  right = pair[i+1:-1]
  return left, right

def magnitude(pair):
  left, right = parts(pair)
  if left.isnumeric():
    left_magn = int(left)
  else:
    left_magn = magnitude(left)
  if right.isnumeric():
    right_magn = int(right)
  else:
    right_magn = magnitude(right)
  return 3*left_magn + 2*right_magn

# ------------------------------------------------------------------------------
# Part 1

# test1 = [[[[[9,8],1],2],3],4]
# test2 = [7,[6,[5,[4,[3,2]]]]]
# test3 = [[1,9],[8,5]]
# test4 = [[6,[5,[4,[3,2]]]],1]
# test5 = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]

# pair = test5

# root = Node(pair[0], pair[1])
# print(root)

# root.reduce()
# print(root)

# ----------------------------------

# test1 = "[[[[[9,8],1],2],3],4]"
# test2 = "[7,[6,[5,[4,[3,2]]]]]"
# test3 = "[[1,9],[8,5]]"
# test4 = "[[6,[5,[4,[3,2]]]],1]"
# test5 = "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"
# test6 = "[[10,1],11]"
# test7 = "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
# test8 = add("[[[[4,3],4],4],[7,[[8,4],9]]]", "[1,1]")
# test9 = "[120,1]"
# pair = test9
# pair = reduce(pair)
# print("final:", pair)

pair = lines[0]
for other in lines[1:]:
  new_pair = add(pair, other)
  new_pair = reduce(new_pair)
  pair = new_pair

print("Part 1:", magnitude(pair))

# ------------------------------------------------------------------------------
# Part 2

largest_magn = float("-inf")
for i in range(len(lines)):
  for j in range(len(lines)):
    if i == j: continue
    pair = add(lines[i], lines[j])
    pair = reduce(pair)
    magn = magnitude(pair)
    if magn > largest_magn:
      largest_magn = magn

print("Part 2:", largest_magn)
