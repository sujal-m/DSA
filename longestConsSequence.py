from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num = {x for x in nums}
        longest = 1
        for x in num:
            if x-1 not in num:
                cnt = 1
                k = x
                while x+1 in num:
                    x = x + 1
                    cnt = cnt + 1
                longest = max(longest, cnt)
        return longest
        
                    