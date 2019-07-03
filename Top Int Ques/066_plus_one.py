class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        n = len(digits)
        # Iterate through the digits backwards
        for i in range(n-1,-1,-1):
            # If it is not the first digit
            if i > 0:
                # If the digit is less than 9
                if digits[i] <9:
                    # Add 1 to it
                    digits[i] += 1
                    return digits
                else:
                    digits[i] = 0
                    continue
            else:
                if digits[i] < 9:
                    digits[i] += 1
                    return digits
                else:
                    digits[i] = 0
                    return [1] + digits
