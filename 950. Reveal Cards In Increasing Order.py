# Apr 13, 2024 950
# solve again
from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        queue = deque([i for i in range(len(deck))])
        res = [0]*len(deck)

        for num in deck:
            idx = queue.popleft()
            res[idx] = num
            if queue:
                queue.append(queue.popleft())
        
        return res