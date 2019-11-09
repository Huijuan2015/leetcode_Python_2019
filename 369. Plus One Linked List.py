# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # reverse link list twice
        newHead = self.reverse(head)

        curr = newHead
        carry = 1
        # while curr:
        #     carry += curr.val
        #     curr.val = carry%10
        #     curr = curr.next
        #     carry = carry//10
            
        prev =  ListNode(0) 
        while curr or carry:
            if curr:
                carry+= curr.val
                curr.val = carry%10
                prev = curr
                curr = curr.next
            else:
                prev.next = ListNode(carry)
            carry = carry//10
            
        # if carry:
        #     curr = ListNode(carry)
        #     curr.next = self.reverse(newHead)
        #     return curr
        return self.reverse(newHead)
    
    def reverse(self, head): #头插
        dummy = ListNode(0)
        curr = head
        
        while curr:
            tmp = curr.next
            curr.next = dummy.next
            dummy.next = curr
            curr = tmp
        
        return dummy.next