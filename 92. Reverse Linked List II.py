# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = prev = ListNode(0)
        dummy.next = head
        for i in range(m-1):
            prev = prev.next
        curr = prev.next
        for i in range(n-m):
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = prev.next
            prev.next = tmp
        return dummy.next