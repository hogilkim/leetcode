# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
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

# Third attempt - solved
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        def dfs(r,c,rdir, cdir):
            robot.clean()
            
            visited.add((r,c))
            
            for _ in range(4):
                if (r+rdir, c+cdir) not in visited and robot.move():
                    dfs(r+rdir, c+cdir, rdir, cdir)
                rdir, cdir = cdir, -rdir
                robot.turnLeft()
            
            robot.turnLeft(); robot.turnLeft();
            robot.move()
            robot.turnLeft();robot.turnLeft();
        
        dfs(0,0,0,1)

        
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        def dfs(x, y, dx, dy):
            robot.clean()
            visited.add((x,y))
            
            for _ in range(4):
                if (x+dx, y+dy) not in visited and robot.move():
                    dfs(x+dx, y+dy, dx, dy)
                robot.turnLeft()
                dx, dy = -dy, dx
            
            robot.turnLeft(); robot.turnLeft();
            robot.move()
            robot.turnLeft(); robot.turnLeft();
        
        dfs(0, 0, 0, 1)