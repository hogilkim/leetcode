class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_sum = sum(matchsticks)
        if total_sum%4: return False
        
        matchsticks.sort(reverse=True)
        
        targets = [total_sum//4]*4
        
        def dfs(match_idx):
            if match_idx == len(matchsticks): return True
            
            for i in range(4):
                if targets[i]>=matchsticks[match_idx]:
                    targets[i] -= matchsticks[match_idx]
                    if dfs(match_idx+1): return True
                    targets[i]+=matchsticks[match_idx]
            
            return False
        
        
        return dfs(0)
    
    