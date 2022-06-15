class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []

        nums = [lower-1]+nums+[upper+1]
        for idx, num in enumerate(nums[:-1]):
            start, end = num + 1, nums[idx+1]-1
            
            if start > end: continue
            elif start == end: res.append(str(start))
            else: res.append(str(start)+"->"+str(end))
                
        
        return res