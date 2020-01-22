# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        self.dirs = [[-1,0],[0,1],[1,0],[0,-1]]
        self.dfs(robot, 0, 0, 0, visited)
        
    def dfs(self, robot, i, j, d, visited):
        if (i,j) in visited:
            return
        
        visited.add((i,j))
        robot.clean()
        for k in range(4):
            new_d = (k+d)%4  要回复方向
            if robot.move():
                x, y = i+self.dirs[new_d][0], j+self.dirs[new_d][1]
                self.dfs(robot, x, y, new_d, visited)
                
                self.goBack(robot)
            robot.turnRight()
            
            
    def goBack(self, robot):
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()
    

    