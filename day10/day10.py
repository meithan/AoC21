# Day 10: 

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
# Part 1

inverse = {'(': ')', '[': ']', '{': '}', '<': '>'}
points1 = {')': 3, ']': 57, '}': 1197, '>': 25137}

def find_corrupt(line):
  stack = []
  for c in line:
    if c in ['(', '[', '{', '<']:
      stack.append(c)
    elif c in [')', ']', '}', '>']:
      if c != inverse[stack[-1]]:
        return c
      else:
        stack.pop()
    
  return None

incomplete_lines = []
score = 0
for line in lines:
  bad_char = find_corrupt(line)
  if bad_char is None:
    incomplete_lines.append(line)
  else:
    score += points1[bad_char]

print("Part 1:", score)

# ------------------------------------------------------------------------------
# Part 2

points2 = {')': 1, ']': 2, '}': 3, '>': 4}

def complete_line(line):
  stack = []
  for c in line:
    if c in ['(', '[', '{', '<']:
      stack.append(c)
    elif c in [')', ']', '}', '>']:
      if c != inverse[stack[-1]]:
        return c
      else:
        stack.pop()
  missing = [inverse[c] for c in stack][::-1]
  return missing

def compute_score(symbols):
  score = 0
  for c in symbols:
    score *= 5
    score += points2[c]
  return score
 
scores = []
for line in incomplete_lines:
  missing = complete_line(line)
  score = compute_score(missing)
  scores.append(score)

scores.sort()
ans2 = scores[len(scores)//2]

print("Part 2:", ans2)
