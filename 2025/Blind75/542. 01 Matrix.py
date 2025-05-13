#BFS 把0 的先放进queue，然后向外扩展到相邻的cell
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        q = deque()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = float('inf')
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            i, j = q.popleft()
            for dx, dy in directions:
                x, y = i +dx, j+dy
                if 0<=x<len(mat) and 0<=y<len(mat[0]) and mat[x][y] > mat[i][j] + 1:
                    mat[x][y] = mat[i][j] + 1
                    q.append((x,y))
        return mat



#DFS, exceed time
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        result = [[-1] * n for _ in range(m)]

        def dfs(i, j, visited):
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited:
                return float('inf')
            if mat[i][j] == 0:
                return 0
            visited.add((i, j))
            min_dist = min(
                dfs(i+1, j, visited),
                dfs(i-1, j, visited),
                dfs(i, j+1, visited),
                dfs(i, j-1, visited)
            )
            visited.remove((i, j))
            return min_dist + 1

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    result[i][j] = 0
                else:
                    result[i][j] = dfs(i, j, set())

        return result