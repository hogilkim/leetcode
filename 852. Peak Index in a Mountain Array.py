class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        
        # log(n) solution
        peak = 0
        peak_index = 0
        left, right = 0, len(arr) -1
        
        while left <= right:
            mid = (left+right)//2
            if arr[mid] > peak:
                peak = arr[mid]
                peak_index = mid
            if arr[mid] > arr[mid-1]:
                left = mid + 1
            else:
                right = mid - 1
                    
        return peak_index
        
        # O(n) solution
        # peak = 0
        # peak_index = 0
        # for i in range(len(arr)):
        #     if arr[i] > peak:
        #         print(i)
        #         peak = arr[i]
        #         peak_index = i
        # return peak_index