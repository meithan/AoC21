# Day 6: 

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
digits_signals_rev = {digits_signals[n]: n for n in digits_signals}

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

letters = "abcdefg"

ans2 = 0
for ins, outs in entries:

  key = {l: set(letters) for l in letters}

  # Decipher key
  
  # 2-letter word is number 1, letters must be one of "cf"
  for word in ins:
    if len(word) == 2:
      for l in word:
        key[l] &= set("cf")

  # 3-letter word is number 7, letters must be one of "acf"
  for word in ins:
    if len(word) == 3:
      for l in word:
        key[l] &= set("acf")

  # 4-letter word is number 4, letters must be one of "bcdf"
  for word in ins:
    if len(word) == 4:
      for l in word:
        key[l] &= set("bcdf")

  # 5-letter words could be numbers 2, 3 or 5
  # The letters that appear in all three must be one of "adg"
  # The letters that appear in only two of the three must be one of "cf"
  # The letters that appear in only one of the three must be one of "be"
  words = []
  for word in ins:
    if len(word) == 5:
      words.append(word)
  words = "".join(words)
  for l in letters:
    if words.count(l) == 3:
      key[l] &= set("adg")
    elif words.count(l) == 2:
      key[l] &= set("cf")
    elif words.count(l) == 1:
      key[l] &= set("be")

  # 6-letter words could be numbers 0, 6 or 9
  # The letters that appear in all three must be one of "abfg"
  # The letters that appear only in two of the three must be one of "cde"
  words = []
  for word in ins:
    if len(word) == 6:
      words.append(word)
  words = "".join(words)
  for l in letters:
    if words.count(l) == 3:
      key[l] &= set("abfg")
    elif words.count(l) == 2:
      key[l] &= set("cde")

  # The only 7-letter word is number 8, but it uses all letters so
  # it is of no use
  
  # Cleanup: eliminate remaining options using deciphered ones
  for l in letters:
    if len(key[l]) == 1:
      for l1 in letters:
        if l1 != l:
          key[l1] -= key[l]
  
  # The key is now fully deciphered! Convert to dict for easier use
  key = {l: key[l].pop() for l in letters}
  # print("key=", key)

  # Now decode the outputs and arrive at the number for this entry
  number = ""
  for word in outs:
    decoded = []
    for l in word:
      decoded.append(key[l])
    decoded = "".join(sorted(decoded))
    digit = digits_signals_rev[decoded]
    number += digit
  number = int(number)
  
  ans2 += number

print("Part 2:", ans2)

