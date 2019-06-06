class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        result = 0

        while i < len(s):
            # Get the value of symbol at s[i]
            #s1 = value(s[i])
            if s[i] == 'I':
                s1 = 1
            if s[i] == 'V':
                s1 = 5
            if s[i] == 'X':
                s1 = 10
            if s[i] == 'L':
                s1 = 50
            if s[i] == 'C':
                s1 = 100
            if s[i] == 'D':
                s1 = 500
            if s[i] == 'M':
                s1 = 1000
            
            if (i+1 < len(s)):
                
                # Get the value of symbol at s[i+1]
                #s2 = value(s[i+1])
                if s[i+1] == 'I':
                    s2 = 1
                if s[i+1] == 'V':
                    s2 = 5
                if s[i+1] == 'X':
                    s2 = 10
                if s[i+1] == 'L':
                    s2 = 50
                if s[i+1] == 'C':
                    s2 = 100
                if s[i+1] == 'D':
                    s2 = 500
                if s[i+1] == 'M':
                    s2 = 1000
                
                # Compare both values
                if s1 >= s2:
                    
                    result = result + s1
                    i = i + 1
                
                else:
                    
                    result = result + s2 - s1
                    i = i + 2
            else:
                result = result + s1
                i = i + 1
                            
        return result
