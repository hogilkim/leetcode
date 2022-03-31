class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr.sort()
        
        missing = 1
        curr = 1
        
        for num in arr:
            while num > curr:
                if missing == k: return curr
                missing += 1
                curr += 1
            curr += 1
        
        return curr + (k-missing)