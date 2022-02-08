# solve again. Monotonic Stack
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        # monotonic stack solution. O(n)
        
        # monotonic increasing stack: returns what is the minimum in the previous array
        res = 0
        stack = []
        inf = float('inf')
        new_nums = [-inf] + nums + [-inf]
        for i, num in enumerate(new_nums):
            
            while stack and new_nums[stack[-1]] > num:
                # k j i -> (i-j)*(j-k)
                j = stack.pop()
                k = stack[-1]
                res -= (i-j)*(j-k)*new_nums[j]            
            stack.append(i)
            
            
        # monotonic decreasing stack: returns what is the maximum in the previous array.
        stack = []
        new_nums = [inf] + nums + [inf]
        for i, num in enumerate(new_nums):
            while stack and new_nums[stack[-1]] < num:
                # k j i
                j = stack.pop()
                k = stack[-1]
                res += (i-j)*(j-k)*new_nums[j]
            stack.append(i)
        
        return res
        
        
        