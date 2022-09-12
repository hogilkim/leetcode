from collections import deque
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = max_score = 0
        
        tokens = deque(sorted(tokens))
        
        
        while tokens:
            # gain score
            if power >= tokens[0]:
                power -= tokens.popleft()
                score += 1
                
            # gain power by consuming score
            else:
                if not score: break
                score -= 1
                power += tokens.pop()
            
            max_score = max(max_score, score)
        
        return max_score
                