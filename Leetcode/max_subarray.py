class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = sum(nums)
        temp = 0
        for val in nums:
            temp += val
            current_sum = max(temp, val)
            if val > temp:
                temp = val
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum
