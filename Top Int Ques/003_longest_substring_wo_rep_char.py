class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        stringlist = []
        max_len = 0

        for letter in s:
            if letter in stringlist:
                stringlist =  stringlist[stringlist.index(letter)+1:]
                
            stringlist.append(letter)
            max_len = max(max_len, len(stringlist))
            
        return max_len
