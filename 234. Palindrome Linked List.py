# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        # reverse  and compare
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # reverse second half!!!
        slow = slow.next
        #reverse slow
        dummy = ListNode(0)
        while slow:
            tmp = slow.next
            slow.next = dummy.next
            dummy.next = slow
            slow = tmp
        left = dummy.next
        right = head
        while left:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
            