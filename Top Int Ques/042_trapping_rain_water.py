class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if height == None:
            return 0
        
        # Two variables for the highest on the left and the 
        # highest on the right
        left_highest = 0
        right_highest = 0
        # Two pointers for the left and right
        left = 0
        right = len(height) - 1
        # A variable for storing the result
        result = 0
        
        # Start from the left 
        while left < right:
            # If the height at left is lesser than that at right
            if (height[left] < height[right]):
                # Check if height at left is greater than left_highest
                if (height[left] >= left_highest):
                    # Update left_highest to height at left
                    left_highest = height[left]
                else:
                    # Add the diff bet left_highest and height at left to result
                    result += left_highest - height[left]
                # Increment left counter by 1
                left += 1
            # If the height at left is greater than that at right
            else:
                # Check if height at right is greater than right_highest
                if (height[right] > right_highest):
                    # Update right_highest to height at right
                    right_highest = height[right]
                else:
                    # Add the diff bet right_highest and height at right to result
                    result += right_highest - height[right]
                # Decrement right counter by 1
                right -= 1
        return result
