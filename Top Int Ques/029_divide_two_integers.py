class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        if dividend > 0:
            signdivid = "plus"
        elif dividend < 0:
            signdivid = "minus"
        else:
            return 0
        
        if divisor > 0:
            signdivis = "plus"
        else:
            signdivis = "minus"
            
        divid = abs(dividend)
        divis = abs(divisor)
        
        if divis > divid:
            return 0
        
        count = 0
        summed = 0
        flag = 0
        
        while True:
            summed += divis
            count += 1
            if divid - summed > divis:
                continue
            else:
                #flag == 1
                break
        
        if signdivid == "plus" and signdivis == "plus":
            return count
        elif signdivid == "minus" and signdivis == "minus":
            return count
        elif signdivid == "plus" and signdivis == "minus":
            return (count - 2*count)
        else:
            return (count - 2*count)
