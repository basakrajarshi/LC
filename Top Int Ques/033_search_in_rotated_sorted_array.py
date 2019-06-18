class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # Find the pivot
        def findPivot(arr, low, high):
            if high < low:
                return -1
            if high == low:
                return low
            
            mid = int((low + high)/2)
            
            if mid < high and arr[mid] > arr[mid + 1]:
                return mid
            if mid > low and arr[mid] < arr[mid -1]:
                return (mid - 1)
            if arr[low] >= arr[mid]:
                return findPivot(arr, low, mid - 1)
            return findPivot(arr, mid + 1, high)
        
        
        # Standard binary search algorithm
        def binarySearch(arr, low, high, key):
            
            if high < low:
                return -1
            
            mid = int((low + high)/2)
            
            if key == arr[mid]:
                return mid
            if key < arr[mid]:
                return binarySearch(arr, low, mid - 1, key)
            else:
                return binarySearch(arr, mid + 1, high, key)
            
        pivot = findPivot(nums, 0, len(nums) - 1)
        
        if pivot == -1:
            return binarySearch(nums, 0, len(nums) - 1, target)
        
        if nums[pivot] == target:
            return pivot
        if nums[0] <= target:
            return binarySearch(nums, 0, pivot - 1, target)
        return binarySearch(nums, pivot + 1, len(nums) - 1, target)
        
