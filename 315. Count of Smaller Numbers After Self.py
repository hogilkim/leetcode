class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if len(nums) < 2: return [0]
        array = sorted([nums[-1],nums[-2]])
        res = [0]
        if nums[-1] >= nums[-2]: res.append(0)
        else: res.append(1)
        
        for i in range(len(nums)-3, -1, -1):
            res.append(self.left_insert(array, nums[i]))
        return reversed(res)
    def left_insert(self, array, inserting):
        l, r = 0, len(array)-1
        
        while l<r:
            mid = (l+r)//2
            if array[mid] < inserting:
                l = mid + 1
            elif array[mid] >= inserting:
                r = mid
                
        if array[l] > inserting:
            while l > 0 and array[l] == array[l-1]:
                l -= 1
                
        else:
            while l < len(array)-1 and array[l] == array[l+1]:
                l += 1
            l += 1
                
        array.insert(l, inserting)
        
        while l > 0 and array[l] == array[l-1]:
            l -= 1
        return l