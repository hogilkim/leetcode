class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def searchLeft(x):
            l, r = 0, len(nums)-1

            while l<=r:
                mid = (l+r)//2

                if x > nums[mid]: l = mid + 1
                else: r = mid - 1
            return l
        
        def searchRight(x):
            l, r = 0, len(nums)-1
            while l<=r:
                mid = (l+r)//2
                
                if x < nums[mid]:
                    r = mid - 1
                else: l = mid + 1
            
            return r
        
        tar = target
        l = searchLeft(tar)
        r = searchRight(tar)
        
        return [l,r] if l<=r else [-1,-1]
    