#!/usr/bin/env python
import alg_1910_sol


if __name__ == '__main__':
  sol = alg_1910_sol.Solution()
  for input_str, part, ans in [
      ("daabcbaabcbc", "abc", "dab"),
      ("axxxxyyyyb", "xy", "ab"),
      ("", "", ""),
    ]:
    rel = sol.removeOccurrences(input_str, part)
    assert ans == rel

  print("All pass!")
