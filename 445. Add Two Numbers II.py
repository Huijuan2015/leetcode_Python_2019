# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 3 stacks
        # 2 stacks with 头插
        stk1 = []
        stk2 = []
        
        while l1:
            stk1.append(l1.val)
            l1 = l1.next
        while l2:
            stk2.append(l2.val)
            l2 = l2.next
            
        carry = 0
        dummy = ListNode(0)
        tail = dummy.next
        while stk1 or stk2 or carry:
            if stk1:
                carry += stk1.pop()
            if stk2:
                carry += stk2.pop()
            dummy.next = ListNode(carry%10)
            dummy.next.next = tail
            tail = dummy.next
            carry = carry//10
        return dummy.next
            