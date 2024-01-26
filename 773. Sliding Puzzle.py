# Solve again Jan 26, 2024 773
next_idx = ((1,3), (0,2,4), (1,5), (0,4), (1,3,5), (2,4))
from collections import deque
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        ROW, COL = len(board), len(board[0])
        SOLVED = [1,2,3,4,5,0]

        curr = (board[i][j] for i in range(ROW) for j in range(COL))

        queue, visited, count = deque([curr]), set(), 0

        while queue:
            for _ in range(len(queue)):
                currboard = list(queue.popleft())
                curridx = currboard.index(0)

                if currboard == SOLVED: return count
                
                for changeidx in next_idx[curridx]:
                    nxtboard = currboard.copy()
                    nxtboard[curridx], nxtboard[changeidx] = nxtboard[changeidx], nxtboard[curridx]
                    nxtboard = tuple(nxtboard)
                    if nxtboard not in visited: 
                        queue.append(nxtboard)
                        visited.add(nxtboard)
            
            count += 1

        
        return -1