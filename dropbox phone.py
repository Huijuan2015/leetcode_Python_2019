
1.find dupl‍‍‍‌‍‌‍‍‍‍‍‍‌‌‍‍‌‌‌icate files given the root directory of a file system
# getPath(string file), 它可以返回这个file/folder的path

# isFile(), get_sub_dir()
# input: "/foo"
def list_dir(path: str) -> List[str]:
    """
    Returns a non-recursive list of entries (files and folders) with
    paths in this directory only. Basically the same functionality as doing “ls”
    or “dir” in a shell
    """
    ret = []
    if not path:
      return ret
    q = deque()
    q.append(path)
    while q:
      curr = q.popleft()
      if isFile(curr) and curr != path:
        ret.append(curr)
      else:
        for p in get_sub_dir(curr):
          q.append(p)
    return ret

def is_dir(path: str) -> bool:
    pass

import hashlib

def findDup(path):
  ret = []
  if not path:  
    return ret
  filesPath = getAllFiles(path)
  dupFilesMap = defaultdict(list)
  BLOCKSIZE = 65536
  for filePath in filesPaths:
    hasher = hashlib.md5() #hashlib.sha256()
    with open(filePath, 'rb') as afile:
      buf.afile.read(BLOCKSIZE)
      while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
    hash_code = hasher.hexdiigest()
    dupFilesMap[hash_code].append(filePath)

  for k, v in dupFilesMap.items:
    if len(v) > 1:
      ret.append(v)
  return ret

#compare file size:
size_mp = {size:[file list]}
import os
os.path.getsize(path)
filename, file_extension = os.path.splitext('/path/to/somefile.ext')

def getAllFiles(path):
  filsPaths = []
  stk = [] # 路径过深的话，用DFS QUEUE
  stk.append(path)
  while stk:
    curr = stk.pop()
    if isFile(curr):
      filesPaths.append(curr)
    else:
      for p in get_sub_dir(curr):
          stk.append(curr+'/'+ p)
  return filesPaths

1. Most memory consuming: MD5, read in files etc
从磁盘读取内容的时候最慢

2.collision:  接著 byte by byte 做比較.   rehash, linkedlist, #extra hash
3.bottleneck:
  md5要scan the whole file -> file size first
4.Symbolic link, same file/dir with diff name, cannot detect cycle by visited…cycle? 
  use absolute path/ skip symbolic link (if we search the whole file system)
5.有没有system层面的考虑来提升性能?默默套了game of life的map reduce。。。 被追问key和value是啥。
如果文件数量非常多怎么办?这个考虑两点优化:第一点要对MD5指纹库查 询并行化，首先是单机内多线程的查询，
文件规模巨大的情况下，就是多机分 布式查询。这个涉及到system design方面了。第二点是考虑文件自身的特性。
文 件大小相同才有可能是重复文件。所以在查询时，首先找到系统中其他相同大 小的文件，然后只跟这些个文件的MD5列表对比，
这样就缩小了查询范围。另 外，对于一些小文件，是否可以有特殊的处理。比如空文件。比如文件特别 小，那是否可以不产生MD5，
直接进行byte比较。这个是开放性的提问，
6.Linux提供了多种API，比如is_regular_file(), is_block_file 等保证确定文件类型
7.如果重复文件查询过程中死机了怎么办?第一点可以考虑checkpointing，定 期保存进度。这样重新启动查询的时候，不需要从零开
始。


2.Find Assessable file‍‌‌‍‌‍‍‍‌‌‌‍‍‌‍‌‌‌‌s in a Linux Tree Structure Syste
folders = [('A', None), ('B', 'A'), ('C', 'B'), ('D', 'B'), ('E', 'A'), ('F', 'E')]
access = set(['C', 'E'])
# find redunduncy
class TreeNode():
  def __init__(self, val):
    self.val = val
    self.children = set()
    self.parent = None
class Access():
  def __init__(self, folders, access):
    self.folders = folders
    self.access = access

  def buildTree(folders):
    root = TreeNode()
    for f1, f2 in folders:
      node1, node2 = TreeNode(f1), TreeNode(f2)
      if not f2:
        root = node1
        continue
      node2.children.add(node1)
      node1.parent = node2
    return root

  def removeRedun(access):
    q = collections.deque()
    q.append(root)
    while q:
      curr = q.popleft()
      for child in curr.children:
        if curr.val in access:
          delete_in_access(child)
        else:
          q.append(curr.children)
    return access

  def delete_in_access(node):
    q = collections.deque()
    q.append(node)
    while q:
      curr = q.popleft()
      if curr.val in access:
        access.discard(curr.val)
      else:
        for child in node.children:
          q.append(child)


# check access
class Access():
  def __init__(self, folders, access):
    self.folders = folders
    self.access = access
  def buildGraph(folders):
    graph = collections.defaultdict(set)
    for folder1, folder2 in folders:
      graph[folder1].add(folder2) # child:parent
    return graph

  def hasAccess(folder):
    if folder in access:
      return True
    if not folder:
      return false 
    return hasAccess(graph[folder])
  def removeExtra(access):
    q = collections.deque(list(access))
    while q:
      acc = q.popleft()
      to_check = acc
      while acc in graph and graph[acc] not in access:
        acc = graph[acc]
      if acc in graph and graph[acc] in access:
        access.remove(to_check)


3.Game of life 【LC289】

- performance bottleneck: disk read/write
- In distributed computing, can use MapReduce, key: top left and bottom right coordinates to represent the rectangle.
每次读三行，处理中间那行
while True:
  start = 0
  with open(filename) as f:
    data = f.readlines()[start:start+3]


# currLine = 0
# board
# with open(file, 'r') as f:
#   while True:
#     cnt = 3
#     while cnt > 0:
#       if f.readline():
#         board.append(f.readline())
#       cnt -= 1
#     #parse lastline to -2 line
#     if len(board) - lastline < 3:
#       break
#     lastline = len(board)

size:
32位int: 4 bytes
64位int: 8 bytes

怎么样来存到disk里面？用bit.
用了bit以后，怎么样来解这个题呢？
一行一行读进去，然后没处理好一行，就写出去。

”如果输入是million * million“  一次读三行，更新数组。
100million 1 interger 4Byte
1 row : 400 million Byte =  = 390625KB  = 381MB
1k = 1024byte
16 G 内存，1T 硬盘

4.Space Panorama
class Sector():
  def __init__(self, x, y):
    self.x = x
    self.y = y

class ListNode():
  def __init__(self, val):
    self.val = val
    self.prev = None
    self.next = None

class DLL():
  def __init__(self):
    self.dummy = ListNode()
    self.tail = self.dummy
    # self.size = 0
  def add_to_head(self, node): #lasted accessed
    self.dummy.next, node.next, node.prev = node, self.dummy.next, self.dummy
    if node.next:
      node.next.prev = node
    if self.tail is self.dummy:
      self.tail = self.tail.next

  def del_node(self, node):
    if not node:
      return
    if node is self.tail:
      self.tail = self.tail.prev
    node.prev.next = node.next
    if node.next:
      node.next.prev = node.prev


class Panarama():
  def __init__(self, m, n):
    self.rows = m
    self.cols = n
    self.sector_photo_dic = {} # can be sector:file path {(x,y):string}
    self.dll = DLL()
    self.sector_node_dic = {} # secotor:node
    #self. size

  def update(sector, photo):
    self.sector_photo_dic[sector] = photo #update sector:photo anyway
    if sector not in self.sector_node_dic: #也不在list中
      node = ListNode(sector, photo)
      # self.dll.add_to_head(node)
      # self.sector_node_dic[sector] = node
    else:
      node = self.sector_node_dic[sector]
      self.dll.del_node(node)
    self.dll.add_to_head(node)
    self.sector_node_dic[sector] = self.dll.dummy.next


  def fetch(sector):
    if sector in self.sector_node_dic:
      node = self.sector_node_dic[sector]
      self.dll.del_node(node)
      self.dll.add_to_head(node)
      self.sector_node_dic[sector] = self.dll.dummy.next
      photo = self.sector_photo_dic[sector]
    return photo

  def getOldest():
      node = self.dll.tail
      photo = self.sector_photo_dic[node]
      self.dll.add_to_head(node)
      self.sector_node_dic[sector] = self.dll.dummy.next
      photo = self.sector_photo_dic[node]
    return photo

rolling hash
假设，一个模式串 P(需要被匹配的串)长度为L，需要在其中查找匹配的串S长度为N。
一种在S中查找P的方式为：

哈希 P 得到 h(P)，时间复杂度 O(L)
从S 的索引为0开始来枚举 S 里长度为 L 的子串，哈希子串并计算出 h(P)'，时间复杂度O(N*L)。
如果一个子串的哈希值 h(P)' 与 h(P) 匹配，将该子串与 P 进行比较，时间复杂度 O(L)
这个做法的时间复杂度为 O(N*L)。我们可以通过使用 Rolling Hash 来优化这种做法。在上述步骤2中，我们看到对于 O(N) 的子串，都花费了 O(L) 来哈希他们，然而可以看到这些子串中很多字符都是重复的。

我们可以利用前一个子串的计算结果哈希值来计算当前子串的哈希值。因此在上述步骤2中，时间复杂度可以优化为O(N)
假设第一个子串哈希值H0 = (S[0] * 10^2 + S[1] * 10^1 + S[2] * 10^0) mod m
则第二个子串哈希值H1 = (10 * H0 - S[0] * 10^3 + S[3] * 10^0) mod m

代码如下：时间复杂度O(length(A) + length(B))
https://www.jianshu.com/p/efca349a218d
5.2d array of "sharpness" values
def fine(grid):
  m, n = len(grid), len(grid[0])
  dp = [_ for _ in range(n)]
  for i in range(m):
    dp[i] = grid[i][0]
  for j in range(1, n):
    tmp = [_ for _ in range(n)]
    for i in range(m):
      if i == 0:
        tmp[i] = max(dp[i], dp[i+1])+grid[i][j]
      elif i == m-1:
        tmp[i] = max(dp[i-1], dp[i]) +grid[i+j]
      else:
        tmp[i] = max(dp[i-1], max(dp[i], dp[i+1])) + grid[i][j]
    dp = tmp
    return dp






























