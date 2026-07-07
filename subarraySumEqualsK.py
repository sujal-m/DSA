from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #optimal approach: prefix_sum and dict
        #prefix_count = p_count, prefix_sum = p_sum
        p_count = {0: 1}
        p_sum = 0
        count = 0

        for num in nums:
            p_sum += num
            if p_sum - k in p_count:
                count += p_count[p_sum - k]
            p_count[p_sum] = p_count.get(p_sum, 0) + 1
        return count


