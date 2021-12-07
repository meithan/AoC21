# AoC21

My solutions for [Advent of Code 2021](https://adventofcode.com/2021). In Python 3.

I'll be updating this as a sort of mini blog whenever I can, commenting on the daily problems.

You can also check out our fancy [custom private leaderboard](https://meithan.net/AoC21/), with medals awarded to the fastest solvers. See (and download/fork!) the project [here](https://github.com/meithan/AoCBoard).

Go to day: [1](#day1) [2](#day2) [3](#day3) [4](#day4) [5](#day5) [6](#day6) [7](#day7)

---

**Day 7**: [The Treachery of Whales](https://adventofcode.com/2021/day/7)<a name="day7"></a>

5m 18s (#?) / ? (#?) - [solution](https://github.com/meithan/AoC21/blob/main/day07)

A straightforward one. Only optimization to mention is using the fact that the sum from 1 to N is equal to N*(N+1)/2. Speeds up computation in Part 2 (although it's still solvable by computing the sum each time).

An idea I had while solving it is that the optimal position is a sort of centroid of the points ... And at least for Part 1 (where normal distance is used) it's indeed true. The *median* of the coordinates is the optimal position!

This problem, that of finding the point that minimizes the sum of distances to a given set of points, is called the *[geometric median]*(https://en.wikipedia.org/wiki/Geometric_median) problem. In 1D, the solution is just the median of the coordinates. But, astonishingly, for 2D and above, it has been shown that the general problem has no closed-form solution (except in special cases, such as 3 or 4 coplanar points). Interesting!

---

**Day 6**: [Lanternfish](https://adventofcode.com/2021/day/6)<a name="day6"></a>

11m 20s (#3709) / 1h 20m 7s (#8323) - [solution](https://github.com/meithan/AoC21/blob/main/day06)

Grrr. I'm sure there's a simple mathematical way to compute this discrete [exponential growth](https://en.wikipedia.org/wiki/Exponential_growth) problem, but I couldn't find it. I solved it through brute force instead, and arriving of a practical strategy for Part 2 took me more than 1 hour.

For Part 1, I simply simulated the process in Python. Start with the list of counters for each fish (the input), and apply the rules successively to the list, appending new fish (so a counter of 8) to the end of the list. For 80 days, this works. Note that you can't iterate directly over the elements of a list and modify the list inside the for loop, so we have to iterate over the index, with the max value given by the list's current size (which also prevents simulating new fish in the same day they're created).

But this is way too slow in Python for Part 2. So I ported the code to C++ to brute force a table of pre-computed growth sizes starting from a single fish and an initial counter of 8. I computed the table up to 256+8 days, to be safe. I used the C++ [`vector`](https://www.cplusplus.com/reference/vector/vector/) class, the equivalent of Python's lists ([dynamic arrays](https://en.wikipedia.org/wiki/Dynamic_array)). To minimize RAM usage, I used [`uint8_t`](https://en.cppreference.com/w/cpp/types/integer) as the data type for the elements of the `vector` (as the individual counters are never greater than 8, they fit in 1 byte, the smallest native data type), and I had to use an long long int (8-byte int) for the size data type, as the size reaches 6,703,087,164 by 264 days, larger than the [max value](https://www.tutorialspoint.com/cprogramming/c_data_types.htm) of a normal 4-byte int. Generating the table up to 264 takes about 45 seconds (as no fish in the input has an initial counter larger than 5, I really only needed up to 261, but oh well).

Having that pre-computed table, it's only a matter of loading the input with the initial counters of all the fish, and computing the total number of fish that will spawn from each one using the table. If the initial counter is X, then we simply look up the value in the table for day N+(8-X) -- with N = 80 for Part 1 and 256 for Part 2. This worked. Oof!

**EDIT**: Well, I'll be damned. I kept thinking of a way to solve it using some mathematics, this being a (discrete) exponential growth problem ... And I quickly realized there's a much simpler way of thinking about the problem! Instead of simulating the individual fish as I did, one simply needs to keep track of *how many* fish are in each "state", where the state of a fish is simply its internal timer, which is a number between 0 and 8.

Say the state of a fish is S. If S > 0, then on the next day its state will be S - 1. If on the other hand S = 0, on the next day its state will be 6, and there will be a new fish with S = 8. Thus, in each iteration all fish with S > 0 simply shift left in the array that counts the states, and those with S = 0 get added to those with S = 6 (the *new* ones with S = 6, which were those with S = 7 at the start of the day), while that same number becomes the new S = 8. The following code carries out this process:

    def simulate_day():
      zeros = fish[0]
      for i in range(8):
        fish[i] = fish[i+1]
      fish[8] = zeros
      fish[6] += zeros

So for instance in the sample input, `3,4,3,1,2`, we initially have one fish in the "1", "2" and "4" states each, and 2 fish in the "3" state. Thus the initial fish states array looks like:

    state     0 1 2 3 4 5 6 7 8
    counts = [0 1 1 2 1 0 0 0 0]

After one day, the counts array becomes:

    state     0 1 2 3 4 5 6 7 8
    counts = [1 1 2 1 0 0 0 0 0]

All values simply shifted to the left. On the next day we have to apply the special rule to the S = 0 counts, while just left-shifting the rest, giving:

    state     0 1 2 3 4 5 6 7 8
    counts = [1 2 1 0 0 0 1 0 1]

The total number of fish is then simply the sum of the array. That's it! Repeating this a total of 80 or 256 times (with the actual input) produces both answers in less then 100 milliseconds (in Python)! I've added a new program implementing this not-dumb solution. Doh!

---

**Day 5**: [Hydrothermal Venture](https://adventofcode.com/2021/day/5)<a name="day5"></a>

14m 17s (#1410) / 21m 36s (#1136) - [solution](https://github.com/meithan/AoC21/blob/main/day05)

Another straightforward problem. For each segment, we set the x and y positions to one end of the segment and march towards the other end. At each step we increment the coordinates by amounts dx and dy, which can be 0, +1 or -1 depending on the sign of the difference between the coordinates of the endpoints. We stop after we've reached the end point. We record all visited points using a dict indexed by coordinates (instead of creating a huge grid spanning the whole domain that will end up with mostly zero counts). We use separate dicts for each Part: we only update that of Part 1 when we're marching along a horizontal or vertical segment (i.e. the end points share a coordinate).

---

**Day 4**: [Giant Squid](https://adventofcode.com/2021/day/4)<a name="day4"></a>

18m 21s (#1028) / 28m 52s (#1408) - [solution](https://github.com/meithan/AoC21/blob/main/day04)

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
