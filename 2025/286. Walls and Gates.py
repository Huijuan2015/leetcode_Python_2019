class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        # gate (i, j) BFS
        queue = deque()
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        while queue:
            i, j = queue.popleft()
            for dir in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                x, y = i + dir[0], j + dir[1]
                if x < 0 or y < 0 or x >= m or y >= n or rooms[x][y] == -1:
                    continue
                elif rooms[x][y] <= rooms[i][j] + 1:
                    continue
                else:
                    rooms[x][y] = rooms[i][j] + 1
                    queue.append((x, y))
        return rooms
            

        