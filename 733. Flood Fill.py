class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
        self.findIsland(image,sr,sc,newColor, image[sr][sc], visited)
        return image
    
    def findIsland(self, image, i, j, newColor, color, visited):
        if i<0 or i >= len(image) or j<0 or j >= len(image[0]) or image[i][j] != color or visited[i][j]:
            return
        image[i][j] = newColor
        visited[i][j] = True
        for dir in [[1,0],[-1,0],[0,1],[0,-1]]:
            x, y = i+dir[0], j+dir[1]
            # print x, y
            self.findIsland(image, x, y, newColor, color, visited)
           