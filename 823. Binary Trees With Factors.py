import collections, math
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        root_map = {}
        res = 0
        
        for num in arr:
            limit = math.sqrt(num)
            way_num = 1
            for root_a in arr:
                if root_a > limit: break
                
                root_b = num/root_a
                
                if root_b in root_map:
                    way_num += root_map[root_a] * root_map[root_b] *\
                    (1 if root_a == root_b else 2)
            
            root_map[num] = way_num
            res += way_num
        
        return res % (10**9+7)
        
        