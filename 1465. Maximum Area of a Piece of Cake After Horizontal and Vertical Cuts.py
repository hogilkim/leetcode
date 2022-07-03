class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = sorted(horizontalCuts+[0,h])
        max_h = max( horizontalCuts[i+1] - horizontalCuts[i] for i in range(len(horizontalCuts)-1) )
                
        verticalCuts = sorted(verticalCuts+[0,w])
        max_v = max( verticalCuts[i+1]-verticalCuts[i] for i in range(len(verticalCuts)-1) )
        
        return (max_h*max_v)%(10**9+7)