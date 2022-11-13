class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        
        memo = {}
        def backtracking(l,r):
            if l == r: return nums[l]
            if (l,r) in memo: return memo[(l,r)]
            
            memo[(l,r)] = max(nums[l] - backtracking(l+1, r), nums[r] - backtracking(l,r-1))
            return memo[(l,r)]
        
        return backtracking(0,len(nums)-1)>=0