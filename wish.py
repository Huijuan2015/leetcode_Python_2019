Given a singly linked list, remove nodes greater than X.
List = 100 → 105 → 50, X = 100
List becomes 100 → 50
Return a reference to the root node of the list after removing 105.

removeNodes has the following parameter(s):
listHead:  a reference to the root node of the singly-linked list
x:  integer, the maximum value to be included in the returned singly-linked list

-------------------------
                  10
                   /  \
                20           30
              /    \       \
            40      50    60       
                  /    \
                70      80

Largest non-connected set in the binary tree. A subset of all tree nodes is an independent set if there is no edge between any two nodes of the subset.

Non-connected set:
1) |10, 40, 50, 60| = 4
2) |10, 40, 70, 80, 60| =  <--- largest non-connected set
3) |20, 30, 70, 80| = 4

{10, 40, 60, 70, 80} and size is 5.

 10
/  \
20  30
可以考虑取[10]或者[20,30]
[10]: 1+recursion(root.left.children)+recursion(root.right.children)
[20,30]: recursion(root.left)+recursion(root.right)

def recursion(root): #return max set length
  if not root:
    return 0
  # if not root.left and not root.right:
  #   return 1
  v1 = 1
  v2 = recursion(root.left) + recursion(root.right)
  if root.left:
    v1 += recursion(root.left.left)+recursion(root.left.right)
  if root.right:
    v1 += recursion(root.right.left)+recursion(root.right.right) 
  return max(v1, v2)





  1. 从在地址栏中输入URL到返回页面这之中都发生了什么？
2. 面试官单拎了上述的一部分关于DNS，域名解析的步骤（也可能是我上一题这边答的很模糊，他才问的）
3. Server 端是怎么处理一个request的
4. 什么是cookie
5. broswer是怎么根据response render页面的
6. Server 和 client 之间是如何建立连接的
7. TCP 和 UDP的区别 （这题我估计是因为我上述问题回答到了TCP，他follow up了一下）
8. 知道什么是SSL么

设计两个API，一个是Insert(string key, int weight)插入一个带权重的key， 
另一个是GetRandom()返回一个任意的之前插入的key，要求返回某个key的概率与之前的Insert的weight成正比，
例如Insert(foo, 1)，Insert(bar, 2)，则此时调用GetRandom()需要按照1/3的概率返回foo，2/3的概率返回bar。
注意key可重复插入，weight不会是负数。


亲戚关系，其他面经有提过，最终的算法要解决的case包括：
A brother B, B sister A, A friend B， B classmate C 这种A B环形,  或者多种关系的情况
上面这个例子，如果是A C的话， 输出[A brother B classmate C, A friend B classmate C]
def getRelation(self, relationStrings, p1, p2): 
        import collections
        relations = [list(relationString.split(' ')) for relationString in relationStrings.split(',')]
        print relations
        mp = collections.defaultdict(lambda:collections.defaultdict(list))
        for relation in relations:
            name1, related, name2 = relation
            mp[name1][name2].append(related)
            mp[name2][name1].append(related)
        """
        mp = {A:{B:(friend, sister,brother),
                 C:(classmate)},
              B:{A:(friend, sister,brother),}
              C:{A:(classmate)}
            }
        """
        res = []
        q = collections.deque()
        q.append((p1, p1+""))
        visited = set()
        while q:
            first, path = q.popleft()
            visited.add(first)
            for second, related in mp[first].items():
                print second, related
                if second not in visited:
                    visited.add(second)
                    for r in related:
                        if second == p2:
                            res.append(path + (r + second))
                            continue
                        q.append((second, path + (r + second)))
                        
        print res



"""
There are n islands connected by m boat rides. Each boat ride starts from island p and arrives at island q with a cost c.
Now given all the islands and boat rides, together with starting island src and the destination dst, find the least cost route from src to dst with up to t stops. (Note: number of stops is the number of island IN BETWEEN src and dst.). If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, t = 1
Output: 200
Explanation: 
The graph looks like this:
0 -> (100) 1 -> (100) 2 
0 -> (500) 2

Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, t = 0
Output: 500
Explanation: 
The graph looks like this:
0 -> (100) 1 -> (100) 2 
0 -> (500) 2

"""
import collections
def findRoute(n, edges, src, dst, t):
    # p1:{p2:cost2, p3:cot3} 
    # {0:{1:100,2:500}..)
    # visited
    # edge cases:
    if n < 2:
        return -1
    # build graph
    graph = collections.defaultdict(lambda: collections.defaultdict())
    # graph = {}
    for edge in edges:
        p1, p2, cost = edge
        graph[p1][p2] = cost
    graph[dst]=None 
    
    # if src or dst not in the graph
    if src not in graph:
        return -1
        
    visited = set()
    ans = float('inf') # min cost in t stops
    q = collections.deque()
    q.append((src, 0, 0)) # (point, dst, stops)
    visited.add(src)
    # BFS
    while q:
        node, currDist, stops = q.popleft()
        # node is valid:
        visited.add(node)
        for next in graph[node]: #1, 2
            # invaid cases
            if stops > t or next in visited or next not in graph:
                continue
            currCost = graph[node][next]
            if next == dst:
                ans = min(ans, currDist+currCost)
                break
            q.append((next, currDist+currCost, stops+1))
    return ans      
            
n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
t = 0   
ans = findRoute(n, edges, src, dst, t)
print ans
# print "Hello World"
