class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        
        diff = float('inf')
        res = []
        
        for i in range(1,len(arr)):
            if diff > abs(arr[i] - arr[i-1]):
                res = []
                res.append([arr[i-1], arr[i]])
                diff = abs(arr[i] - arr[i-1])
            
            elif diff == abs(arr[i] - arr[i-1]):
                res.append([arr[i-1], arr[i]])
        
        return res