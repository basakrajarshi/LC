class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x >= 2**31-1 or x <= -2**31: 
            return 0
        else:
            numinstr = str(x)
            if x >= 0 :
                revstr = numinstr[::-1]
                #revst = str(reversed(numinstr))
            else:
                temp = numinstr[1:] 
                temp2 = temp[::-1]
                #temp2 = str(reversed(numinstr))
                revstr = "-" + temp2
            if int(revstr) >= 2**31-1 or int(revstr) <= -2**31: 
                return 0
            else: 
                return int(revstr)
