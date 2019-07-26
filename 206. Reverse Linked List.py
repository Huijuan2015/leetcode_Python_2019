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
        
        # dummy = ListNode(0)
        # curr = head
        # while curr:
        #     tmp = curr.next # 原链表
        #     curr.next = dummy.next
        #     dummy.next = curr
        #     curr = tmp
        # return dummy.next
            
          