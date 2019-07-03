class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
        if x == 1:
            return 1
        
        res = 2
        while res*res <= x: 
            if res**2 == x:
                return res
            res += 1
            
        return res-1
