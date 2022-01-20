# solutions on Neetcode and discussions does not work

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k or int(sum(nums)/k) != sum(nums)/k: return False #[1]
        N = len(nums)
        nums.sort(reverse=True) #[2]
        
        def dp(mask, cur, memo): # Top-down DP with memoization
            if mask == 0: return cur == 0 #[3]
            elif cur == 0: return dp(mask, sum(nums)/k, memo) #[4]
            if (mask, cur) not in memo:
                res = False
                for bit in range(N): #[5]
                    if mask & (1 << bit): #[6]
                        if nums[bit] > cur: continue # Writing this to be more explicit, for easy-understanding
                        if dp(mask ^ (1 << bit), cur-nums[bit], memo): #[7]
                            res = True
                            break
                memo[(mask, cur)] = res
            return memo[(mask, cur)] 
        return dp(2**N-1, sum(nums)/k, dict()) #[8]
# class Solution:
#     def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
#         if len(nums) < k or int(sum(nums)/k) != sum(nums)/k:
#             return False
#         nums.sort(reverse=True)
#         parts = [sum(nums)/k]*k
#         return self.dfs(parts, nums, 0)
    
#     def dfs(self, parts, nums, idx):
#         if idx == len(nums):
#             return not sum(parts)
#         for i in range(len(parts)):
#             if parts[i] >= nums[idx]:
#                 parts[i] -= nums[idx]
#                 if self.dfs(parts, nums, idx+1):
#                     return True
#                 parts[i] += nums[idx]
# # solve again
# # first attempt - Jan 19, 2022
# class Solution:
#     def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
#         if sum(nums)%k: return False
#         target = sum(nums)/k
#         nums.sort(reverse=True)
#         used = [False]*len(nums)
        
#         def backtracking(i, k, subsetSum):
#             if k == 0:
#                 return True
#             if subsetSum == target:
#                 return backtracking(0, k-1, 0)
        
#             for j in range(i, len(nums)):
#                 if used[j] or subsetSum + nums[j] > target:
#                     continue
#                 used[j] = True
#                 if backtracking(j+1, k, subsetSum + nums[j]):
#                     return True
#                 used[j] = False
#             return False
        
#         return backtracking(0, k, 0)