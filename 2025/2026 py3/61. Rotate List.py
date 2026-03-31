# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        n = 1 # linklist length
        oldTail = head #find tail, record length
        while oldTail.next:
            oldTail = oldTail.next
            n += 1
        
        k = k % n
        if k == 0:
            return head
        
        #find new tail, new head
        move = n-k-1 #到新尾巴的步数  用实际例子算一下
        newTail = head
        
        while move > 0:
            newTail = newTail.next
            move -= 1
        
        newHead = newTail.next
        oldTail.next = head
        newTail.next = None
        return newHead

            

