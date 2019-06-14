# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        # Inititate an array to store the merged linked list
        arr = []
        
        # Initiate a header for the result linked list
        result = ListNode(0)
        result_tail = result
        
        # Go through each linkedlist and store all the elements
        # in the array 
        for ll in lists:
            while ll != None:
                if ll != None:
                    v1 = ll.val
                    ll = ll.next
                    arr.append(v1)
                else:
                    ll = None
        
        # Sort the array
        arr.sort()
        
        # Construct the new result linked list from the array
        for ch in arr:
            result_tail.next = ListNode(ch)
            result_tail = result_tail.next
            
        return result.next
            
