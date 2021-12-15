# AoC21

My solutions for [Advent of Code 2021](https://adventofcode.com/2021). In Python 3.

I'll be updating this as a sort of mini blog whenever I can, commenting on the daily problems.

You can also check out our fancy [custom private leaderboard](https://meithan.net/AoC21/), with medals awarded to the fastest solvers. See (and download/fork!) the project [here](https://github.com/meithan/AoCBoard).

Go to day: [1](#day1) [2](#day2) [3](#day3) [4](#day4) [5](#day5) [6](#day6) [7](#day7) [8](#day8) [9](#day9) [10](#day10) [11](#day11) [12](#day12) [13](#day13) [14](#day14) [15](#day15)

---

**Day 15**: [Chiton](https://adventofcode.com/2021/day/15)<a name="day15"></a>

44m 37s (#3056) / 1h 2m 15s (#2027) - [solution](https://github.com/meithan/AoC21/blob/main/day15)

A straightforward graph search problem. For practice, I decided to code A* search to solve it, using the Manhattan distance as heuristic (which is [consistent](https://en.wikipedia.org/wiki/Consistent_heuristic)). The node-to-node distance cost is the risk of the arrival node.

For Part 2, I built the extended risk grid and used that instead of the original in the A* search.

---

**Day 14**: [Extended Polymerization](https://adventofcode.com/2021/day/14)<a name="day14"></a>

32m 37s (#5576) / 18h 17m 19s (#27788) *(solved next day)* - [solution](https://github.com/meithan/AoC21/blob/main/day14)

Ah, another problem where the naive, brute force solution is simply completely impractical for Part 2. Those are always fun.

The size of the "polymer" essentially doubles at every step (the exact size obeys the recurrence N_{k+1} = 2\*N_k - 1, which solves to 2^k\*(N0 - 1) + 1), so after 40 steps it's about 2^40 ≈ 10^12 times larger. Hence, just *storing* the final polymer (with 1 letter = 1 byte) requires a few TB of space, so it most definitely won't fit in RAM (but it could conceivably be stored on disk and processed in chunks) ... Not to mention the massive time required at later stages to fully process the polymer to do one step. Hence, producing the final sequence in full is just not practical (apparently somebody managed to [brute force Part 2](https://www.reddit.com/r/adventofcode/comments/rfzq6f/2021_day_14_solutions/hoimmxq/?utm_source=share&utm_medium=web2x&context=3) through heavy optimization and parallel computing).

In Part 1, where only 10 steps are required, I just implemented the polymer insertion algorithm, produced the final polymer sequence, and counted the letters ([collections.Counter](https://docs.python.org/3/library/collections.html#collections.Counter) is useful for that).

For Part 2 a completely different approach was needed, and I couldn't find it immediately so I left it for the next day (hence the solve time). They key is to think somewhat along the lines of the Lanternfish in [Day 6](#day6): we don't need to keep all individual elements (in this case letters of the polymer sequence), but only *counts* of them, since that's all that's asked.

In this case in particular, the key insight is to keep a count of *pairs* of letters, and that during a step each pair will produce two new pairs: if AB -> C, then the pair AB will yield new pairs AC and CB. Hence, at each step we simply go over each pair and transfer its count to each of its children pairs (while discarding the count of the original pair).

Consider the example template: NNCB. This can be split into pairs NN, NC and CB, so the counts are initially {NN: 1, NC: 1, CB: 1}; a [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict) is a handy data structure for this. To advance one step we apply the "expanded" rules NN -> (NC, CN), NC -> (NB, BC) and CB -> (CH, HB), resulting in the new pair counts {NC: 1, CN: 1, NB: 1, BC: 1, CH: 1, HB: 1}. Note the we're not storing the exact sequence of overlapping pairs, and hence we can't reconstruct the exact polymer sequence -- but we *can* determine the counts of the letters.

To do so, we keep in mind that all letters in the sequence, except the first and last, are actually counted twice (due to the overlapping). So we just count all letters present in the counted pairs, and divide each result by 2. Finally, we add an extra count for the first and last letters of the polymer sequence (which do not change during the process) since those weren't counted twice. And voila! The algorithm yields the correct letters counts after 40 steps in under 30 ms.

---

**Day 13**: [Transparent Origami](https://adventofcode.com/2021/day/13)<a name="day13"></a>

12m 50s (#713) / 14m 39s (#365) - [solution](https://github.com/meithan/AoC21/blob/main/day13)

A cute problem. We keep the dots in a set so that duplicates are automatically handled. When folding, we mirror the relevant coordinate of the points around the fold line and add them to a new set. For instance, for a fold along x the new x coordinate is x' = fold_coord - (x - fold_coord); y remains the same.

For Part 2, instead of writing code to draw the points on the terminal in ASCII art, I opted to just use [Matplotlib](https://matplotlib.org/). After resizing, the answer appeared:

<p align="center">
<img src="https://github.com/meithan/AoC21/blob/main/day13/day13_sol.png" alt="drawing" width="500"/>
</p>

---

**Day 12**: [Passage Pathing](https://adventofcode.com/2021/day/12)<a name="day12"></a>

23m 41s (#2957) / 42m 32s (#2178) - [solution](https://github.com/meithan/AoC21/blob/main/day12)

A twist on standard maze-solving problems. I wrote a modified [depth-first search](https://en.wikipedia.org/wiki/Depth-first_search) where we don't keep mark nodes as visited (since we're allowed to visit large caves multiple times) and instead check each path before extending it. We also don't stop after finding the end node, just save it and keep going (standard when looking for all paths).

We first load the input creating the adjacency list of the caves, stored as a "name": <set of reachable caves> dict. Then, for Part 1:

- Create an empty list to work as the stack.
- Also create an empty list to store the found paths.
- Instead of working with maze nodes, we work with full paths. We initially push the path containing just "start" to the stack.
- Then while the stack is not empty:
    - Pop a path from the stack
    - If the tail node is "end", add this path to the list of found paths (but keep going)
    - For each node adjacent to the tail node:
        - If the child node is uppercase (a large cave), or if it's lowercase (small cave) but it's not yet in the considered path, we create a new path by adding the child node to the path, and we push this new path to the stack.

This will finish as long as no two large caves are adjacent, because if that happens we'll have an infinite loop which the problem statement does not specify how to handle. But this is not the case in any of the inputs.

For Part 2, we do basically the same except for the rule on when to create and push a new path. We only do so if one of the following is True:

- It's a large cave (uppercase)
- It's a small cave (lowercase) and it's not yet in the path
- It's a small cave that is already in the path, but no small cave in the path appears twice (we have to check for that every time)

This is not very efficient but the input is not very large. Optimizations would be 1) keeping an additional faster data structure to check for inclusion in the path, 2) having a way to mark a path as having visited two caves already so we don't have to check again every time.

---

**Day 11**: [Dumbo Octopus](https://adventofcode.com/2021/day/11)<a name="day11"></a>

23m 57s (#1775) / 26:03 (#1588) - [solution](https://github.com/meithan/AoC21/blob/main/day11)

Although it was an easy problem a mistake slowed me down. To simulate the evolution of the problem (it's debatable whether this constitutes a [cellular automaton](https://en.wikipedia.org/wiki/Cellular_automaton), but it's certainly very similar) the energies are stored in a 2D array (just nested lists). Then the algorithm for each iteration is as follows:

- Increment all energies by one. Any octopus that goes above 9 --one that will flash-- is added to a Python set (`to_flash`).
- Create a new empty set to store octopi that have already flashed (`has_flashed`).
- Then, as long as `to_flash` is not empty:
    - Pop the next octopus, and add it to `has_flashed`.
    - Reset the octopus' energy to zero.
    - Loop over the neighbors *that have not flashed* (by checking `has_flashed`), and increment them by one. If any goes over 9, we add it to `to_flash`

The length of `has_flashed` after each step is the number of octopi that flashed, and adding those up solves Part 1.

For Part 2 I was smelling blood: I feared that the number of steps until all the octopi flash simultaneously would be astronomical, making it impractical to find the moment by direct simulation. But I followed the right strategy: before starting to look for an alternative solution, just try if direct simulation solves the problem. And for this case it did. So solving Part 2 took me only two more minutes (the time to read it and write the few extra lines of code).

We were fortunate to avoid that curveball. Is there a way to predict the number of steps neeed for all octopi to flash from the initial condition without simulation?

---

**Day 10**: [Syntax Scoring](https://adventofcode.com/2021/day/10)<a name="day10"></a>

17m 49s (#3901) / 24m 44s (#2659) - [solution](https://github.com/meithan/AoC21/blob/main/day10)

This is a variation of the the classic parens matching problem, which is solved with a[stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)); we can use a simple Python list for that. The idea is simple. For each line, we go over its characters and:

- If it's an opening character (`(`, `[`, `{`, `<`) we push it into the stack.
- If it's a closing character (`)`, `]`, `}`, `>`), we check what's at on top of the stack:
    - If it's a matching character, we pop it out of the stack, and continue;
    - If it's *not* a matching character, the line is *corrupt*.

If the process reaches the end of the line without finding a corrupt character, then if the stack is empty the line is complete and valid (which is not the case for any line in the problem), and if the stack is not empty the line is incomplete (but not corrupt).

In Part 1 we only do this process until an invalid closing character is found, and use it to compute the score. The non-corrupt lines are set aside.

In Part 2, for each incomplete line we go over the complete process and after that the stack contains the ordered list of unmatched opening characters. The missing closing characters are just the coresponding characters but in reverse (easy to do in Python).

---

**Day 9**: [Smoke Basin](https://adventofcode.com/2021/day/9)<a name="day9"></a>

1h 34m 54s (#12188) / 2h 55m 32s (#10901) - [solution](https://github.com/meithan/AoC21/blob/main/day09)

An easy problem, but I had D&D night so I coded Part 1 in short bursts during the session, and Part 2 only after it finished. So times are not representative of the time spent.

We read the heightmap into a 2D array. For Part 1 we simply check all locations to see if they're lower than all their neighbors (the wording is that it has to be *strictly* lower, so if a point's height ties with any of its neighbors, it's not a low point). We handle edges of the map by always going over all four neighbors, but skipping any that is outside the domain.

For Part 2, this is a straightforward example of graph traversal where the goal is to find the [connected components](https://en.wikipedia.org/wiki/Component_(graph_theory)), since that is what the basins are. The idea is to start from each of the low points and see what other points are reachable by always going *up*, ignoring points with a height of 9 (as they're not part of any basin).

Both [depth-first search](https://en.wikipedia.org/wiki/Depth-first_search) (DFS) and [breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search) (BFS) can be used for this. I opted for BFS here, for which Python's built-in FIFO [queue.Queue](https://docs.python.org/3/library/queue.html#queue-objects) class is very handy. I usually prefer non-recursive implementations of these graph algorithms since that completely avoids recursion depth limits.

This is just one way to implement BFS:

1. We start with each of the low points previously found in Part 1, and we find its associated basin.
2. In each case, we create an initially empty [set](https://docs.python.org/3/tutorial/datastructures.html#sets) (O(1) inclusion lookups on average) in which we'll store the points visited, which constitute the basin, and we initialize a queue to store the points still be to checked. We add the low point to the queue.
3. While the queue is not empty (which is written very literally in Python):
  1. We get the next point from the queue, and add it to the visited set.
  2. We check each of its neighbors. If the neighbor is already in the visited set, we skip it. If it's not, we check whether its height is *higher* than the point we just extracted. If so, we push the neighbor to the queue. Note that points with a height of 9 are just ignored.
4. When the queue is finally empty we stop, and the points in the visited set constitute the basin.

I also plotted the height map and the basins, just for fun:

<p align="center">
<img src="https://github.com/meithan/AoC21/blob/main/day09/day09_map1.png" alt="drawing" width="500"/>
</p>

<p align="center">
<img src="https://github.com/meithan/AoC21/blob/main/day09/day09_map2.png" alt="drawing" width="500"/>
</p>


---

**Day 8**: [Seven Segment Search](https://adventofcode.com/2021/day/8)<a name="day8"></a>

16m 27s (#4529) / 1h 50m 30s (#5472) - [solution](https://github.com/meithan/AoC21/blob/main/day08)

A problem that required careful reading to understand it. And one for which Part 2 (it was kinda obvious what it was gonna be after reading Part 1) took me way too long to solve due to choosing the wrong strategy to approach the problem. Both solutions are really not difficult or long to code.

For Part 1, we check only the output words of each entry:

* If a word has 2 letters, it must be digit 1
* If a word has 3 letters, it must be digit 7
* If a word has 4 letters, it must be digit 4
* If a word has 7 letters, it must be digit 8

We then simply count how many 1s, 4s, 7s and 8s were found and that's it.

For Part 2, I ended up solving it using <s>two</s> different strategies, but it took me way too much alternating between the two and making them work.

Strategy 1: Brute force

This is a simple [substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher) with a 7-letter alphabet (the letters corresponding to the seven segments, 'abcdefg'), so there are 7! = 5040 possible keys. Hence, it's completely feasible to brute force the problem by trying them all. In each entry, for a given trial key we go over each of the 10 signal patterns and see if it deciphers to one of the digits under that key. If it works for all patterns, we've found the correct key. We then decipher the output values and solve the problem. This breaks the key in a couple of seconds. Using [itertools.permutations](https://docs.python.org/3/library/itertools.html#itertools.permutations) is a nice compact way to iterate over all permutations of 'abcdefg' (instead of the seven nested fors).

Strategy 2: Breaking the cipher by successive elimination ([code](https://github.com/meithan/AoC21/blob/main/day08/day08_alt.py))

The second, more clever strategy is to work out the key by elimination by analizing the 10 signal patterns and applying restrictions derived from the letters contained in each digit. We create a mapping of the cipher letters 'abcdefg' to Python [sets](https://docs.python.org/3/library/stdtypes.html#set) containing all remaining possibilites, initially all letters. Then we go over each of the 10 encoded signal patterns, and narrow down the options for each letter by applying the following rules:

* The only 2-letter word is number 1, so each of its cipher letters must be one of 'cf'
* The only 3-letter word is number 7, so each of its cipher letters must be one of 'acf'
* The only 4-letter word is number 4, so each of its cipher letters must be one of 'bcdf'
* The three 5-letter words correspond to numbers 2, 3 and 5, and we notice how many times the letters appear in these numbers:
  * The cipher letters that appear in all three must be one of 'adg'
  * The cipher letters that appear in only two of the three must be one of 'cf'
  * The cipher letters that appear in only one of the three must be one of 'be'
* The three 6-letter words correspond to 0, 6 and 9, and again we notice how many times the letters appear in these numbers:
  * The cipher letters that appear in all three must be one of 'abfg'
  * The cipher letters that appear only in two of the three must be one of 'cde'
* The only 7-letter word is number 8, but since it uses all seven letters it is of no use so we just ignore it

To apply each rule we simply update the set corresponding to each cipher letter by computing the [set intersection](https://en.wikipedia.org/wiki/Intersection_(set_theory)) with the letters in the restriction; the `&` operator works as intersection when applied to Python sets. For instance, if at some point 'a' has been narrowed down to {'a', 'b', 'c', 'g'}, and we find an 'a' in a 3-letter word which means 'a' must translate into one of 'acf', then we compute the set intersection {'a', 'b', 'c', 'g'} & {'a', 'c', 'f'} = {'a', 'c'}. Thus, 'b' and 'g' have been ruled out.

Once these rules have been applied, most cipher letters end up with a single remaining option, and we can use these solved letters to solve for the remaining ones. With this, the key has been deciphered, and we can now solve the problem by decoding the outputs of each entry.

**Update**: Strategy 3: Deducing the numbers without breaking the cipher ([code](https://github.com/meithan/AoC21/blob/main/day08/day08_alt2.py))

People on Reddit were commenting how they solved the problem without actually fully breaking the cipher (which is also what one my friends did), so I decided to try that solution strategy.

As shown in Part 1, from the 10 given encoded numbers in each entry the numbers 1, 4, 7 and 8 are immediately identifiable, as they have unique numbers of segments: 3, 4, 3 and 7, respectively. The other six numbers either have 5 segments (2, 3 and 5) or 6 segments (0, 6 and 9). The key is that some of them contain enough unique segment patterns to deduce which is which, and after finding those the remaining ones can be deduced. Here's the solution algorithm:

1. As for Part 1, we begin by identifying what cipher words correspond to the numbers 1, 4, 7 and 8 based on the number of letters (segments that are on):
    - The only word with 2 letters is number **1**
    - The only word with 4 letters is number **4**
    - The only word with 3 letters is number **7**
    - The only word with 7 letters is number **8**
2. We look at the three 5-letter words. The only of the three that contains the 2-letter combination corresponding to 1 (which we already found) is number **2**.
3. We now look at the three 6-letter words. The only one that *doesn't* contain the pattern for 1 is the number **6**.
3. The only 6-letter word that contains the pattern for 3 is the number **9**.
4. The remaining 6-letter word is the number **0**.
5. The only 5-letter word that *is contained in* the pattern for 6 (which we previously found) is number **5**.
6. The remaining 5-letter word is number **2**.

We now know the cipher patterns that correspond to each number and can thus solve the remaining portion of the problem. To determine whether a given pattern is contained in another pattern, an idiomatic way is to store the patterns (the letters) in Python sets, for which `<=` works as [subset](https://en.wikipedia.org/wiki/Subset) operator. For instance `{'a', 'b'} <= {'a', 'b', 'c'}` yields `True`.

---

**Day 7**: [The Treachery of Whales](https://adventofcode.com/2021/day/7)<a name="day7"></a>

5m 18s (#1654) / 8m 38s (#1290) - [solution](https://github.com/meithan/AoC21/blob/main/day07)

A straightforward one. Only optimization to mention is using the fact that the sum from 1 to N is equal to N*(N+1)/2. Speeds up computation in Part 2 (although it's still solvable by computing the sum each time).

An idea I had while solving it is that the optimal position is a sort of centroid of the points ... And at least for Part 1 (where normal distance is used) it's indeed true. The *median* of the coordinates is the optimal position!

This problem, that of finding the point that minimizes the sum of distances to a given set of points, is called the *[geometric median](https://en.wikipedia.org/wiki/Geometric_median)* problem. In 1D, the solution is just the median of the coordinates. But, astonishingly, for 2D and above, it has been shown that the general problem has no closed-form solution (except in special cases, such as 3 or 4 coplanar points). Interesting!

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
