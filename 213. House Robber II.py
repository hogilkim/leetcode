class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums_sublist):
            print(nums_sublist)
            bigger_val = 0
            smaller_val = 0
            for num in nums_sublist:
                temp = max(smaller_val + num, bigger_val)
                smaller_val = bigger_val
                bigger_val = temp
            return bigger_val

        
        max1 = helper(nums[1:])
        max2 = helper(nums[:-1])
        
        return max(nums[0], max1, max2)