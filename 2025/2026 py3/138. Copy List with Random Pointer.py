"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        old_to_new = {}
        curr = head
        # 建立映射表：原节点 -> 新节点
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        # 根据原链表的连接关系，给新节点“接线”
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next) #为了防止curr.next key 不存在，用get. 
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next
        return old_to_new[head]