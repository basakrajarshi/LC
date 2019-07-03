class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        
        result = []
        
        # Arrange all intervals by last digit
        inter = sorted(intervals, key=lambda x: x[0])
        
        # Iterate through all the pairs:
        for pair in inter:
            # If results is empty or last pair in results
            # does not overlap
            if not result or result[-1][1] < pair[0]:
                # Append the newest pair from inter
                result.append(pair)
            else:
                # Merge the interval and append to result
                result[-1][1] = max(result[-1][1], pair[1])
                
        return result
