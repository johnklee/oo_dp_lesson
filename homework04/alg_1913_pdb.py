#!/usr/bin/env python
import pdb   # 1) Import PDB module
from typing import List


class Solution:
    # 1913. Maximum Product Difference Between Two Pairs
    # https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
    def maxProductDifference(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums, reverse=True)
        return sorted_nums[0] * sorted_nums[1] - sorted_nums[-1] * sorted_nums[-2]


if __name__ == '__main__':
  sol = Solution()
  pdb.set_trace() # 2) Set breakpoint
  for nums, ans in [
      ([5,6,2,7,4], 34),
      ([4,2,5,9,7,4,8], 64),
      ([3,4,5], 8),
      ([1,2], 0),
      ([1], 0),
    ]:
    rel = sol.maxProductDifference(nums)
    assert ans == rel
