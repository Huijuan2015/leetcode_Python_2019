# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode('-INF')
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next
        
        头插
        # dummy = ListNode(0)
        # curr = head
        # while curr:
        #     tmp = curr.next # 原链表
        #     curr.next = dummy.next
        #     dummy.next = curr
        #     curr = tmp
        # return dummy.next
        
        # curr->curr.next
        # dummy->curr.next->curr->curr.next.next
        # dummy->1
        tmp = curr.next
        curr.next = dummy.next
        dummy.next = curr
        curr = tmp

recursive
        if not head or not head.next:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
          