class Solution(object):
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return ""
        if digits == "1":
            return ""
        if len(set(digits)) == 1 and int(digits[0]) == 1:
            return ""
        
        d = {'2':['a','b','c'],
             '3':['d','e','f'],
             '4':['g','h','i'],
             '5':['j','k','l'],
             '6':['m','n','o'],
             '7':['p','q','r', 's'],
             '8':['t','u','v'],
             '9':['w','x','y', 'z']}
        
        def backtrack(combo, nextdigits):
            # if there are no more digits to check
            if len(nextdigits) == 0:
                # the combination is complete
                res.append(combo)
            # otherwise there are digits to check
            else:
                print(nextdigits)
                # go through all letters which map the next digit
                for letter in d[nextdigits[0]]:
                    # append the current letter to the combination 
                    # and proceed to the next digits
                    backtrack(combo + letter, nextdigits[1:])
                    
        res = []
        if digits is not None:
            backtrack("",digits)
        #print(res)
        return res
