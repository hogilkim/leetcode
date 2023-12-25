# Solve again
# Dec 25, 2023 84
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        heights.append(0)
        stack = [] # (height, idx)

        for idx, h in enumerate(heights):
            start = idx
            while stack and stack[-1][0] > h:
                prev_h, prev_idx = stack.pop()
                max_area = max(max_area, ( prev_h ) * ( idx - prev_idx ) )
                start = prev_idx
            
            stack.append((h, start))
        return max_area