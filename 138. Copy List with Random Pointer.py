"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """   
        #map original node: new node
        from collections import defaultdict
        mp = defaultdict(lambda:Node(0, None, None))
        curr = head
        mp[None] = None  !!dict 默认没有None key
        while curr:
            mp[curr] = Node(curr.val, None, None)
            curr = curr.next
        curr = head
        while curr:
            mp[curr].next = mp[curr.next]
            mp[curr].random = mp[curr.random]
            curr = curr.next
        return mp[head]


straight forward:
def copyRandomList(self, head):
    dic = dict()
    m = n = head
    while m:
        dic[m] = RandomListNode(m.label)
        m = m.next
    while n:
        dic[n].next = dic.get(n.next) 普通dict必须用get
        dic[n].random = dic.get(n.random)
        n = n.next
    return dic.get(head)