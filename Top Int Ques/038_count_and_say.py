class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        
        s = "11"
        for i in range(3, n + 1):
            s += '$'
            l = len(s)
            
            count = 1
            
            temp = ""
            
            for j in range(1,l):
                
                if (s[j] != s[j-1]):
                    
                    temp += str(count)
                    
                    temp += s[j-1]
                    
                    count = 1
                    
                else:
                    
                    count += 1
                    
            s = temp
        return s
        
