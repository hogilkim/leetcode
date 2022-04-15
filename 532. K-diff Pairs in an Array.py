class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:            
        nums = sorted(nums)
        
        candidates = set()
        pair = set()
        count = 0
        for num in nums:
            if num in candidates and (num-k,num) not in pair:
                count += 1
                pair.add((num-k, num))
            candidates.add(num+k)
    
        return count