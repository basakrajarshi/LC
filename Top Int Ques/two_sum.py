class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for index,item in enumerate(nums):
            ch = target - item
            if ch not in d:
                d[item] = index
            else:
                return [d[ch],index]
