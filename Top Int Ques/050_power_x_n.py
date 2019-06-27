class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        
        if n == 0:
            return 1
        
        if n == 1 or x == 1:
            return x
        
        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1
        
        if n >= 2**31 - 1 or n <= (-2)**31:
            return 0
        
        i = 0
        result = 1
        m = abs(n)
        while i < m:
            result = result * x
            i += 1
            
        if n < 0:
            final = 1/result
        else:
            final = result
            
        return final
