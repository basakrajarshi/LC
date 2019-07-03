class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        results = [0] * (n+1)
        results[0:3] = [0,1,2]
        
        # Insert the fibonacci number sequence
        for i in range(3, n+1):
            results[i] = results[i-1] + results[i-2]
            
        return(results[n])
