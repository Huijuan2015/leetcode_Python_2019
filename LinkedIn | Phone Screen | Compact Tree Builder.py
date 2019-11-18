
 
    # class Node<T> {
    # private final T data;
 
    # private final List<Node<T>> children;
 
    # public Node(T data, List<Node<T>> children) {
    #     this.data = data;
    #     this.children = children;
    # }
 
    # public T getData() {
    #     return data;
    # }
 
    # public List<Node<T>> getChildren() {
    #     return children;
    # }



 class Solution(object):
    def compact(self, root, n):
        from collections import deque
        self.q = deque()
        self.toArr(root)

        newRoot = Node(self.q.popleft())
        curr = [newRoot]
        while curr:
            nextLevel = []
            for node in curr:
                i = 0
                childList = []
                while i < n and self.q:
                    childList.append(Node(self.q.popleft()))
                    i+=1
                node.chilren = childList
                nextLevel.extend(childList)
            curr = nextLevel if self.q else []
        return newRoot


# BFS turn the tree to a 1D array
    def toArr(self, root):
        if not root:
            return
        level = [root]

        while level:
            nextLevel = []
            for node in level:
                self.q.append(node.getData())
                if node.children:
                    nextLevel.extend(getChildren(node))
            level = nextLevel



