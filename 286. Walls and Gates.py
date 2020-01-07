class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        self.dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        self.INF = 2147483647
        # -1： 不走
        # INF： 继续
        # 0 return
        if not rooms or not rooms[0]:
            return rooms
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                # print rooms[i][j]
                if rooms[i][j] == 0:
                    self.helper(rooms, i j, 0)
        return rooms               
            
    def helper(self, rooms, i, j, length): #return shortest length from all dirs
        if i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[0]) or rooms[i][j] < length:
            return 
        rooms[i][j] = length
        for dir in self.dirs:
            x, y = i+dir[0], j+dir[1]
            self.helper(rooms, x, y, length+1)
        
