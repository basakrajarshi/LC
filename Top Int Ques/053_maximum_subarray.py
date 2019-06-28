class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = nums[0]
        maximum_sum = nums[0]
        
        for i in range(1,len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            maximum_sum = max(maximum_sum, current_sum)
            
        return maximum_sum
