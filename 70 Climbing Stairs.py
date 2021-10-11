class Solution(object):
    def climbStairs(self, n):
        
        ways_list = [1,2]
        
        for i in range(3,n+1):
            ways_list.append(ways_list[i-3] + ways_list[i-2])
        
        return ways_list[n-1]