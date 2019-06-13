# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        arr = []
        
        result = ListNode(0)
        result_tail = result
        
        while l1 != None:
            if l1 != None:
                v1 = l1.val
                l1 = l1.next
                arr.append(v1)
            else:
                l1 = None
            
        while l2 != None:
            if l2 != None:
                v2 = l2.val
                l2 = l2.next
                arr.append(v2)
            else:
                l2 = None
                
        arr.sort()
        
        for num in arr:
            result_tail.next = ListNode(num)
            result_tail = result_tail.next
            
        return result.next
