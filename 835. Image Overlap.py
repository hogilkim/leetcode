from collections import defaultdict
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        a = []
        b = []
        
        N = len(img1)
        
        for row in range(N):
            for col in range(N):
                if img1[row][col] == 1: a.append((row,col))
                if img2[row][col] == 1: b.append((row,col))
                    
        
        diff_dic = defaultdict(int)
        
        for point1 in a:
            for point2 in b:
                diff_dic[(point1[0]-point2[0], point1[1]-point2[1])] += 1
        
        return max(diff_dic.values()) if diff_dic.values() else 0