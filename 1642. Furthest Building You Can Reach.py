import collections, heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        reached = 0
        
        max_heap = [] # bricks_used
        heapq.heapify(max_heap)
        
        for idx, h in enumerate(heights[:-1]):
            if heights[idx+1] <= h: 
                reached+=1
                continue
                
            diff = heights[idx+1] - h
            if bricks < diff:
                if not ladders: break
                
                # ========= Same as Below if statement======
                # if not max_heap or diff > -1*max_heap[0]:
                #     ladders -= 1
                # else:
                #     bricks += -1*heapq.heappop(max_heap)
                #     heapq.heappush(max_heap, -1*diff)
                #     bricks -= diff
                #     ladders -= 1
                # ===============================
                #=============Same as Above if-else
                if max_heap and diff < -1*max_heap[0]:
                    bricks += -1*heapq.heappop(max_heap)
                    heapq.heappush(max_heap, -1*diff)
                    bricks -= diff
                ladders -= 1
                # =================================
            
            else:
                bricks -= diff
                heapq.heappush(max_heap, -1*diff)
            reached += 1
        
        return reached
            
            