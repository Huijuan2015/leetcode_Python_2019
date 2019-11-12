# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k < 0:
            return
        slow = head
        fast = head
        l = 1
        while fast.next:
            fast = fast.next
            l+=1
        # print l
        fast = head
        for i in range(k%l):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        rotateHead = slow.next
        if not rotateHead:
            return head
        slow.next = None

        fast.next = head

        
        return rotateHead