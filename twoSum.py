class Solution:
    def twoSum(self, nums, target: int):
        #optimal approach
        nums_with_index = [(num, idx) for idx, num in enumerate(nums)]
        nums_with_index.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            curr_sum = nums_with_index[left][0] + nums_with_index[right][0]
            if curr_sum == target:
                return [nums_with_index[left][1], nums_with_index[right][1]]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1 