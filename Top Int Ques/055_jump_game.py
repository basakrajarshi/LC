class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        
        end = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= end:
                end = i
            print(end)
        return end == 0
