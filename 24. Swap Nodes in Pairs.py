# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Recursively?
        if not head or not head.next:
            return head
        next = head.next
        behind = next.next
        next.next = head
        head.next = self.swapPairs(behind)
        #head = next
        return next
#         dummy = prev = ListNode(0)
#         dummy.next = head
#         while head and head.next:
#             # swap head and head.next
#             tmp = head.next
#             head.next = tmp.next
#             tmp.next = head
            
#             # prev connection
#             prev.next = tmp
#             head = head.next
#             prev = tmp.next
#         return dummy.next
        
       