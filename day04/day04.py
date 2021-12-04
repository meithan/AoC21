# Day 04:

import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

class Board:
  def __init__(self, rows):
    self.grid = rows
    self.marks = []
    for i in range(5):
      self.marks.append([False]*5)
    self.won = False
  def mark_number(self, number):
    for i in range(5):
      for j in range(5):
        if self.grid[i][j] == number:
          self.marks[i][j] = True
  def is_winning(self):
    for row in self.marks:
      if all(row):
        return True
    for j in range(5):
      marks = [self.marks[i][j] for i in range(5)]
      if all(marks):
        return True
    return False
  def score(self):
    s = 0
    for i in range(5):
      for j in range(5):
        if self.marks[i][j] == False:
          s += self.grid[i][j]
    return s
  def __repr__(self):
    s = ""
    for row in self.grid:
      s += " ".join([str(x) for x in row]) + "\n"
    return s

# Read (and possibly pre-process) input
numbers = []
boards = []
with open(sys.argv[1]) as f:
  numbers = [int(x) for x in f.readline().strip().split(",")]
  rows = []
  for line in f:
    if line == "\n":
      if len(rows) > 0:
        boards.append(Board(rows))
        rows = []
    else:
      rows.append([int(x) for x in line.strip().split()])
if len(rows) > 0:
  boards.append(Board(rows))

# ------------------------------------------------------------------------------
# Parts 1 and 2

def play_bingo():
  first_winner = None
  boards_won = 0
  for n in numbers:
    for board in boards:
      if not board.won:
        board.mark_number(n)
    for board in boards:
      if not board.won:
        if board.is_winning():
          if first_winner is None:
            print("FIRST WINNER")
            print(board)
            first_winner = board
            ans1 = board.score() * n
          board.won = True
          if boards_won == len(boards) - 1:
            print("LAST WINNER")
            print(board)
            ans2 = board.score() * n
            return ans1, ans2
          boards_won += 1

ans1, ans2 = play_bingo()
print("Part 1:", ans1)
print("Part 2:", ans2)
