class Solution(object):
    # Find and return the left-most or right-most index at which 
    # 'target' is in sorted array 'nums' courtesy a modified binary search
    def boundary_index(self, nums, target, left):
        low = 0
        high = len(nums)
        
        while low < high:
            middle = (low + high) // 2
            if nums[middle] > target or (left == True and target == nums[middle]):
                high = middle
            else:
                low = middle + 1
                
        return low
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_index = self.boundary_index(nums, target, True)
        
        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]
        
        right_index = self.boundary_index(nums, target, False) - 1
        
        return [left_index, right_index]
