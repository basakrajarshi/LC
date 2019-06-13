# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Initiate the result 
        result = ListNode(0)
        result_tail = result
        
        # Initiate an array to store the ll
        lltoarray = []
        
        # Traverse the linked list
        while head != None:
                
            if head != None:
                # Fetch the value
                v1 = head.val
                # Go to the next pointer
                head = head.next
                # Append the value to the array
                lltoarray.append(v1)
            else:
                head = None
        
        # Remove the nth element from the end of the list
        lltoarray.pop(-n)
        
        # Traverse the list
        for i in lltoarray:
            # Store the value in result_tail next pointer
            result_tail.next = ListNode(i)
            # Increment the pointer
            result_tail = result_tail.next
            
        return result.next
