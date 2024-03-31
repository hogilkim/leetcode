# Solve again
# Mar 31, 2024 930
# Solutions sol
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = {0: 1}
        curr_sum = 0
        total_subarrays = 0
        
        for idx, num in enumerate(nums):
            curr_sum += num
            print(curr_sum - goal)
            if curr_sum - goal in count:
                total_subarrays += count[curr_sum - goal]
            count[curr_sum] = count.get(curr_sum, 0) + 1
            print(count)
            print("total_subarrays", total_subarrays)

        return total_subarrays

# Neetcode Sol
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    
        def calc_subarr_less_than_or_equal_to_goal(x):
            if x < 0: return 0
            res = 0

            total_sum = 0
            l = 0

            for r in range(len(nums)):
                total_sum += nums[r]

                while total_sum > x:
                    total_sum -= nums[l]
                    l += 1
                res += r - l + 1
            
            return res
        

        return calc_subarr_less_than_or_equal_to_goal(goal) - calc_subarr_less_than_or_equal_to_goal(goal-1)


