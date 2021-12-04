# AoC21

My solutions for [Advent of Code 2021](https://adventofcode.com/2021). In Python 3.

I'll be updating this as a sort of mini blog whenever I can, commenting on the daily problems.

You can also check out our fancy [custom private leaderboard](https://meithan.net/AoC21/), with medals awarded to the fastest solvers. See (and download/fork!) the project [here](https://github.com/meithan/AoCBoard).

Go to day: [1](#day1) [2](#day2) [3](#day3) [4](#day4)

---

**Day 4**: [Giant Squid](https://adventofcode.com/2021/day/4)<a name="day4"></a>

18m 21s (#1028) / 28m 52 (#1408) - [solution](https://github.com/meithan/AoC21/blob/main/day04)

A straightforward problem, just requiring to write the code to simulate the game as described. Not proud of my speed.

---

**Day 3**: [Binary Diagnostic](https://adventofcode.com/2021/day/3)<a name="day3"></a>

4m 12s (#298) / 14m 40s (#359) - [solution](https://github.com/meithan/AoC21/blob/main/day03)

A simple string manipulation problem -- though there's probably a sneakier binary-arithmetic way of solving it. The only bitwise operation I used was to obtain epsilon directly from gamma by inverting the bitsring in gamma by [XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR)'ing it with a mask of all '1's (so XOR'ing the numeric value of gamma with 2^s-1, where s is the number of bits).

Part 2 took me way too long to code, and I should've leveraged zip and [collections.Counter](https://docs.python.org/3/library/collections.html#collections.Counter) instead of counting everything by hand.

---

**Day 2**: [Dive!](https://adventofcode.com/2021/day/2)<a name="day2"></a>

3m 35s (#1583) / 5m 13s (#985) - [solution](https://github.com/meithan/AoC21/blob/main/day02)

Another warm-up. I got both gold medals on our private leaderboard out of pure luck, honestly, as I beat the runner-up by only a few seconds!

---

**Day 1**: [Sonar Sweep](https://adventofcode.com/2021/day/1)<a name="day1"></a>

3m 11s (#1552) / 6m 04s (#973) - [solution](https://github.com/meithan/AoC21/blob/main/day01)

As usual Day 1 is just a warm-up. Not very impressed with the time it took me to correctly write a few lines of code, but oh well. At least I got both gold medals on our [private leaderboard](https://meithan.net/AoC21/).
