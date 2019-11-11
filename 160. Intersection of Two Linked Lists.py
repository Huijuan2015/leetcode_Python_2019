# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 对齐2个 先取得2个长度
        def getLen(head):
            l = 0
            curr = head
            while curr:
                curr = curr.next
                l += 1
            return l
                
        l1 = getLen(headA)
        l2 = getLen(headB)
        # print l1, l2
        if l2 < l1:
            headA, headB =  headB, headA
            l1, l2 = l2, l1
         #A短B长
        i = l2- l1
        while i > 0 and headB:
            headB = headB.next
            i -= 1
        # print headA.val, headB.val
        #现在AB一样长了
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return
            
        