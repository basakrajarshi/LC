class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # Initialize dictionary to store results
        result = {}
        # Iterate through each word in the input list
        for word in strs:
            # Sort the letters in the word and store in a string
            sortedwordtolist = sorted(word)
            # Convert the list to an immutable tuple
            tup = tuple(sortedwordtolist)
            # Store the word as a value in a list corresponding to the tuple
            # storing the letters constituting the word in the results 
            # dictionary
            if tup not in result:
                result[tup] = [word]
            else:
                result[tup].append(word)
        # Return the values as a list (of lists, since each value is a list)
        return result.values()
        
        
