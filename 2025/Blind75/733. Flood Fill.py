class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if not image:
            return
        oldColor = image[sr][sc]
        self.fill(image, sr, sc, oldColor)
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == '#':
                    image[i][j] = color
        return image
                

    def fill(self, image, sr, sc, oldColor):
        if sr < 0 or sr >= len(image) or sc < 0 or sc>= len(image[0]):
            return
        if image[sr][sc] != oldColor or image[sr][sc] == '#':
            return
        image[sr][sc] = '#'
        self.fill(image, sr, sc+1, oldColor)
        self.fill(image, sr, sc-1, oldColor)
        self.fill(image, sr-1, sc, oldColor)
        self.fill(image, sr+1, sc, oldColor)


class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if not image:
            return
        oldColor = image[sr][sc]
        visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
        self.fill(image, sr, sc, color, oldColor, visited)
        return image
                

    def fill(self, image, sr, sc, color, oldColor, visited):
        if sr < 0 or sr >= len(image) or sc < 0 or sc>= len(image[0]) or image[sr][sc] != oldColor or visited[sr][sc]:
            return

        image[sr][sc] = color
        visited[sr][sc] = True
        # self.fill(image, sr, sc+1, color, oldColor, visited)
        # self.fill(image, sr, sc-1, color, oldColor, visited)
        # self.fill(image, sr-1, sc, color, oldColor, visited)
        # self.fill(image, sr+1, sc, color, oldColor, visited)
        for dir in [[1,0], [-1,0], [0,1], [0,-1]]:
            x, y = sr + dir[0], sc+dir[1]
            self.fill(image, x, y, color, oldColor, visited)
