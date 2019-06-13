class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        
        # -------------
        # USING A STACK
        # -------------
        
        open_brackets = ["[", "{", "("]
        close_brackets = ["]", "}", ")"]
        
        # Initiate an epmty stack
        st = []
        
        # Iterate through each element in the string
        for ch in s:
            # If the element is in open_brackets
            if ch in open_brackets:
                # Add it to the stack
                st.append(ch)
            # If the element is in close_brackets    
            elif ch in close_brackets:
                # Find the index of the element in close_brackets
                ind = close_brackets.index(ch)
                # If stack is not empty and element at same index in open_brackets is the same element at the bottom of the stack
                if ((len(st) > 0) and (open_brackets[ind] == st[-1])):
                    # Remove the last element from the stack
                    st.pop()
                else:
                    return False
        # If the stack is empty
        if len(st) == 0:
            # Return True
            return True
            
