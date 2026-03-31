# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)

        #find lefttail, midhead, midtail, rigthhead
        leftTail = dummy

        for _ in range(left-1):
            leftTail = leftTail.next

        midHead = leftTail.next

        prev = None #另外定义一个prev比较清晰
        curr = midHead
        for _ in range(right-left+1):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        leftTail.next = prev
        midHead.next = curr
        return dummy.next

用 for loop比较好


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0, head)
        rightTail = dummy
        midLen = right-left+1
        while left-1 > 0:
            rightTail = rightTail.next
            left -= 1
        midHead = rightTail.next

        #reverse mid这段 midHead-midTail
        prev = None
        curr = midHead 
        
        while midLen > 0:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            midLen -= 1
        
        leftHead = curr

        rightTail.next = prev
        midHead.next = leftHead
    
        return dummy.next

        






