# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        #get k length and reverse
        if not head:
            return head
        fast = head
        i = 1
        while i < k and fast.next:
            fast = fast.next
            i+=1
        newHead = fast.next
        if i != k:
            return head
        fast.next = None
        retHead, retTail = self.reverse(head)
        retTail.next = self.reverseKGroup(newHead, k)
        return retHead
    
    def reverse(self, head):
        if not head or not head.next:
            return [head, head]
        dummy = ListNode(0)
        tail = dummy.next
        curr = head
        while curr:
            tmp = curr.next
            dummy.next = curr
            curr.next = tail
            tail = curr
            curr = tmp
        return [dummy.next, head]