class TreeNode(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.parent = None

class Solution(object):
  def lca(self, p, q):
    if not p or not q:
      return

    h1 = self.getHeight(p)
    h2 = self.getHeight(q)
    if h1 > h2: #1比2短
      h1, h2 = h2, h1
      p, q = q, p

    while h1 < h2:
      if not q:
        return
      q = q.parent
      h2 -= 1
    和linkedlist一样，先把两个node拉到同一个高度，再一起往前走
    while p and q:
      if p == q:
        return p
      p = p.parent
      q = q.parent
    return


  def getHeight(self, node):
    height = 0

    while node:
      node = node.parent
      height+=1
    return height

