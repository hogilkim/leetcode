# solved Jan 15, 2022
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        
        result = []
        
        def backtracking(part, part_sum):
            if len(part) >= k:
                if part_sum == n:
                    result.append(part.copy())
                return
            
            prev = part[-1] if part else 0
            
            for i in range(prev + 1, 10):
                if part_sum + i <= n:
                    part.append(i)
                    backtracking(part, part_sum + i)
                    part.pop()
            
        
        backtracking([], 0)
        return result