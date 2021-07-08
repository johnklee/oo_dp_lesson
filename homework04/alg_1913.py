#!/usr/bin/env python
from typing import List
import pdb

class Solution:
    # 1913. Maximum Product Difference Between Two Pairs
    # https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
    def maxProductDifference(self, nums: List[int]) -> int:
        if len(nums) <= 1:
          return 0
        else:
          sorted_nums = sorted(nums, reverse=True)
          return sorted_nums[0] * sorted_nums[1] - sorted_nums[-1] * sorted_nums[-2]

if __name__ == '__main__':
  sol = Solution()

  #pdb.set_trace()
  for nums, ans in [
      ([5,6,2,7,4], 34),
      ([4,2,5,9,7,4,8], 64),
      ([3,4,5], 8),
      ([1,2], 0),
      ([1], 0),
    ]:
    rel = sol.maxProductDifference(nums)
    assert ans == rel
