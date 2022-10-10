from collections import deque
class Solution:
    def racecar(self, target: int) -> int:
        # moves, currpos, speed
        
        queue = deque([(0,0,1)])
        
        visited = set()
        
        while queue:
            for _ in range(len(queue)):
                moves, currpos, speed = queue.popleft()
                if currpos == target: return moves
                
                if (currpos, speed) in visited: continue
                
                visited.add((currpos, speed))
                                
                # accelerate
                queue.append((moves+1, currpos + speed, speed*2))
                
                # R
                if (currpos+speed>target and speed > 0) or (currpos+speed<target and speed<0):
                    queue.append((moves+1, currpos, speed//abs(speed)*-1))
        
        