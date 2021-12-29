class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # solve again. Probably cannot solve if not seen this before.
        slow, fast = 0, 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        slow2 = 0    
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
            
        # Space (O(n)) solution
        # return (sum(nums) - sum(list(set(nums))))//(len(nums) - len(set(nums)))