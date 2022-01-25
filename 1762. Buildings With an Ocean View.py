class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        output, currMax = [], 0
        
        for i in range(len(heights)-1, -1,-1):
            if heights[i] > currMax:
                output.append(i)
                currMax = heights[i]
        
        return reversed(output)