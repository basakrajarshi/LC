class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]*-1
            j = i + 1
            k = n - 1
            while j < k:
                if nums[j] + nums[k] == target:
                    result.append([nums[i], nums[j], nums[k]])
                    j = j + 1 
                    while j < k and nums[j] == nums[j-1]:
                        j = j + 1
                elif nums[j] + nums[k] < target:
                    j = j + 1
                else:
                    k = k - 1
        return result
