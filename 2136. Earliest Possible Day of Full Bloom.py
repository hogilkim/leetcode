class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        res = 0
        
        for gt, pt in sorted(zip(growTime, plantTime)):
            res = max(res, gt) + pt
        
        return res