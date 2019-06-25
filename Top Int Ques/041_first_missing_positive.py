class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 1
        
        flag = 0
        
        while flag == 0:
            if result not in nums:
                return result
            else:
                result += 1
