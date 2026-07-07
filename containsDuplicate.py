class Solution:
    def containsDuplicate(self, nums) -> bool:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        for value in freq.values():
            if value >= 2:
                return True
        return False