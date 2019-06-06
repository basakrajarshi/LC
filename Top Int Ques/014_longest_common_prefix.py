class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        
        if not strs:
            return result
        
        if len(strs) == 1:
            return strs[0]
        
        # Find the length of the shortest word
        wordlengths = []
        for word in strs:
            wordlengths.append(len(word))
        minlength = min(wordlengths)
        
        if minlength == 0:
            return result
        
        length = 0
        
        while length < minlength:
            #words = 0
            letters = []
            for word in strs:
                letters.append(word[length])
            print(letters)
            if all(x == letters[0] for x in letters):
                result = result + letters[0]
                length += 1
            else:
                return result
        return result
