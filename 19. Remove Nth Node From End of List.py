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
        #先走n步, 如果头结点可能被删，就要定义dummy
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = head
        
        while fast:
            if n > 0:
                n -= 1
            else:
                slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next