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
    ins = [x.strip() for x in tokens[0].strip().split(" ")]
    outs = [x.strip() for x in tokens[1].strip().split(" ")]
    entries.append((ins, outs))

digits_signals = {
  "0": "abcefg",
  "1": "cf",
  "2": "acdeg",
  "3": "acdfg",
  "4": "bcdf",
  "5": "abdfg",
  "6": "abdefg",
  "7": "acf",
  "8": "abcdefg",
  "9": "abcdfg"
}
digits_signals_rev = {v: k for k, v in digits_signals.items()}

# ------------------------------------------------------------------------------
# Part 1

counts = {"1": 0, "4": 0, "7":0, "8":0}
for ins, outs in entries:
  for word in outs:
    if len(word) == 2:
      counts["1"] += 1
    elif len(word) == 4:
      counts["4"] += 1
    elif len(word) == 3:
      counts["7"] += 1
    elif len(word) == 7:
      counts["8"] += 1

tot_counts = sum(counts.values())

print("Part 1:", tot_counts)

# ------------------------------------------------------------------------------
# Part 2

def decode(ins, key):
  decoded = []
  for word in ins:
    word1 = []
    for l in word:
      word1.append(key[l])
    word1 = "".join(sorted(word1))
    if word1 not in digits_signals_rev:
      return False
    else:
      decoded.append(digits_signals_rev[word1])
  return int("".join(decoded))

letters = "abcdefg"

total = 0
for ins, outs in entries:
  for key in itertools.permutations(letters):
    key = {letters[i]: key[i] for i in range(7)}
    found = decode(ins, key)
    if found != False:
      value = decode(outs, key)
      total += value

print("Part 2:", total)

