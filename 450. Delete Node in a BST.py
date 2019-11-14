# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        # recursive
        # 1) no child, del
        # 2) 1 child, return left/right as result
        # 3) 2 chilren/replace with right-child-leftmost, then delete that val-> 1)
        
        def deleteNode(root, key):
  if not root: # if root doesn't exist, just return it
    return root
  if root.val > key: # if key value is less than root value, find the node in the left subtree
    root.left = deleteNode(root.left, key)
  elif root.val < key: # if key value is greater than root value, find the node in right subtree
    root.right= deleteNode(root.right, key)
  else: #if we found the node (root.value == key), start to delete it
    if not root.right: # if it doesn't have right children, we delete the node then new root would be root.left
      return root.left
    if not root.left: # if it has no left children, we delete the node then new root would be root.right
      return root.right
               # if the node have both left and right children,  we replace its value with the minmimum value in the right subtree and then delete that minimum node in the right subtree
    temp = root.right
    mini = temp.val
    while temp.left:
      temp = temp.left
      mini = temp.val
    root.val = mini # replace value
    root.right = deleteNode(root.right,root.val) # delete the minimum node in right subtree
  return root

            