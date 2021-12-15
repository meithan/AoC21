# Day 14: Extended Polymerization

from collections import Counter, defaultdict
import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
rules = {}
with open(sys.argv[1]) as f:
  template = f.readline().strip()
  f.readline()
  for line in f:
    pair, result = line.strip().split(" -> ")
    rules[pair] = result

template0 = template

# ------------------------------------------------------------------------------
# Part 1

for step in range(1,10+1):
  new_template = ""
  for i in range(len(template)-1):
    pair = template[i:i+2]
    new_template += template[i] + rules[pair]
  new_template += template[-1]
  template = new_template

counts = Counter(template)
mc = counts.most_common()
ans1 = mc[0][1] - mc[-1][1]

print("Part 1:", ans1)

# ------------------------------------------------------------------------------
# Part 2

## Count the size after 40 steps
# N = len(template0)
# for i in range(1,40+1):
#   N = 2*N - 1
#   print(f"{i} {N:,}")

# Transform rules to pair -> (pair1, pair2)
rules2 = {p: (p[0]+rules[p], rules[p]+p[1]) for p in rules.keys()}

# Initialize pair counts
counts = defaultdict(int)
for i in range(len(template0)-1):
  pair = template0[i:i+2]
  counts[pair] += 1
first = template0[0]
last = template0[-1]

# Do iterations
for i in range(1,40+1):
  new_counts = defaultdict(int)
  for pair,num in counts.items():
    pair1, pair2 = rules2[pair]
    new_counts[pair1] += num
    new_counts[pair2] += num
  counts = new_counts

# Count letters
letters = defaultdict(int)
for pair, num in counts.items():
  a,b = pair
  letters[a] += num
  letters[b] += num
# Each letter is counted twice ...
for l in letters:
  letters[l] //= 2
# ... except the first and last
letters[first] += 1
letters[last] += 1

# Sort letter counts
mc = [(l, letters[l]) for l in letters]
mc.sort(key=lambda x: x[1], reverse=True)
ans2 = mc[0][1] -mc[-1][1]

print("Part 2:", ans2)
