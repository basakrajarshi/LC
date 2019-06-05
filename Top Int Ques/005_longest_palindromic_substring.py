class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        
        result = ""
        for i in range(len(s)):
            j = i + 1
            while (j <= len(s) and len(result) <= len(s[i:])):
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(result):
                    result = s[i:j]
            j += 1
            
        return result
