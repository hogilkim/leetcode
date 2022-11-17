class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        top_right_y = min(ay2, by2)
        top_right_x = min(ax2, bx2)
        
        bottom_left_y = max(ay1, by1)
        bottom_left_x = max(ax1, bx1)
        
        x_overlap = max(top_right_x - bottom_left_x,0)
        y_overlap = max(top_right_y - bottom_left_y, 0)        
        return ((ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1)) - x_overlap*y_overlap