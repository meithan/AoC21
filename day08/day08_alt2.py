# Day 8: Seven Segment Search

import itertools
import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
entries = []
with open(sys.argv[1]) as f:
  for line in f:
    tokens = line.strip().split("|")
    codes = [set(x.strip()) for x in tokens[0].strip().split(" ")]
    outputs = [x.strip() for x in tokens[1].strip().split(" ")]
    entries.append((codes, outputs))

# ------------------------------------------------------------------------------
# Parts 1 and 2

ans1 = ans2 = 0
for codes, outputs in entries:
  
  keys = {str(n): None for n in range(10)}
  len5 = []; len6 = []
  
  for code in codes:
    
    # Numbers 1, 4, 7, 8 (they have a unique number of segments)
    # and split remaining into 5-letter and 6-letter codes
    if len(code) == 2:
      keys['1'] = code
    elif len(code) == 3:
      keys['7'] = code
    elif len(code) == 4:
      keys['4'] = code
    elif len(code) == 7:
      keys['8'] = code
    elif len(code) == 5:
      len5.append(code)
    elif len(code) == 6:
      len6.append(code)

  # Number 3: only 5-letter code that contains the pattern for 1
  for code in len5:
    if keys['1'] <= code:
      keys['3'] = code
      break

  # Number 6: only 6-letter code that doesn't contain the pattern for 1
  for code in len6:
    if not keys['1'] <= code:
      keys['6'] = code
      break

  # Number 9: only 6-letter code that contains the patterrn for 3
  for code in len6:
    if keys['3'] <= code:
      keys['9'] = code
      break  

  # Number 0: the remaining 6-letter code
  for code in len6:
    if code != keys['6'] and code != keys['9']:
      keys['0'] = code
      break

  # Number 5: only 5-letter code that is contained in the pattern for 6
  for code in len5:
    if code <= keys['6']:
      keys['5'] = code
      break  

  # Number 2: remaining 5-letter code
  for code in len5:
    if code != keys['3'] and code != keys['5']:
      keys['2'] = code
      break

  # Reverse keys
  rev_keys = {"".join(sorted(v)):k for k,v in keys.items()}

  # Decode outputs
  decoded = [rev_keys["".join(sorted(c))] for c in outputs]

  # Counts for Part 1
  for c in ['1', '4', '7', '8']:
    ans1 += decoded.count(c)

  # Add number for Part 2
  ans2 += int("".join(decoded))

print("Part 1:", ans1)
print("Part 2:", ans2)


