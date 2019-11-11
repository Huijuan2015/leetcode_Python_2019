# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        #1 for odd, 2 for even
        odd = head
        even = head.next
        dummy1.next = odd
        dummy2.next = even
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = dummy2.next
        return dummy1.next
            
            
            