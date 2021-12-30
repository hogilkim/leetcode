class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # solve again
        # dp solution 
        dp = {}
        
        def dfs(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = dfs(i+1, total + nums[i]) + dfs(i+1, total-nums[i])
            
            return dp[(i,total)]
        
        return dfs(0,0)
        
        
        # time limit exceeded solution
        
#         self.counter = 0
        
#         def dfs(addition, add, i):
#             addition += add
#             #print(addition)
#             if i == len(nums) - 1:
#                 if addition == target:
#                     self.counter += 1
#                 return
            
#             dfs(addition, nums[i+1], i+1)
#             dfs(addition, -nums[i+1], i+1)
#         dfs(0, nums[0], 0)
#         dfs(0, -nums[0], 0)
#         return self.counter