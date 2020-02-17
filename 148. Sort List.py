# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        first = head
        second = slow.next
        slow.next = None
        
        l = self.sortList(first)
        r = self.sortList(second)
        return self.merge(l, r)

        
    def merge(self, h1, h2):
        dummy = ListNode(None)
        curr = dummy
        while h1 and h2:
            if h1.val < h2.val:
                curr.next = h1
                h1 = h1.next
            else:
                curr.next = h2
                h2 = h2.next
            curr = curr.next
        curr.next = h1 if h1 else h2 
        return dummy.next