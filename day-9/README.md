# Day 8: Resonant Collinearity

Given a map of antennas, output the unique antinodes produced by each antenna.
Antennas are marked as single letters or numbers.

```
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
```

## Part 1

Input is an antenna map. Output count of all unique antinode locations. An antinode occurs at any point that is perfectly in line with two antennas of the same frequency - but only when one of the antennas is twice as far away as the other. This means that for any pair of antennas with the same frequency, there are two antinodes, one on either side of them.

```
......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#.
```

## Part 2

Input is an antenna map. Output count of all unique antinode locations. However, a change of rules. An antinode occurs at any grid position exactly in line with at least two antennas of the same frequency, regardless of distance

```
##....#....#
.#.#....0...
..#.#0....#.
..##...0....
....0....#..
.#...#A....#
...#..#.....
#....#.#....
..#.....A...
....#....A..
.#........#.
...#......##
```