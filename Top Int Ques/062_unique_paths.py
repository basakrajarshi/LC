class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        # From every point, the point to the diagonal bottom right 
        # (if it exists) can be reached in two ways 
        
        numpaths = [[0 for i in range(n)] for j in range(m)]
        print(numpaths)
        
        for i in range(m):
            numpaths[i][0] = 1
            
        for j in range(n):
            numpaths[0][j] = 1
            
        for i in range(1,m):
            for j in range(1,n):
                numpaths[i][j] = numpaths[i][j-1] + numpaths[i-1][j]
                
        return(numpaths[m-1][n-1])
    
