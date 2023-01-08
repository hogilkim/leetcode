from collections import Counter
import math
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        return max(-1, sum(math.ceil(val/3) if val > 1 else float('-inf') for val in Counter(tasks).values()))