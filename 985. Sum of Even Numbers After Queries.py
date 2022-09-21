class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evensum = sum(num for num in nums if not num%2)
        res = []
        for val, idx in queries:
            new_val = nums[idx] + val
            #odd to even
            if nums[idx]%2 and new_val%2 == 0:
                evensum += new_val
            # even to odd
            elif nums[idx]%2 == 0 and new_val%2:
                evensum -= nums[idx]
            
            # even to even
            elif nums[idx]%2 == 0 and new_val%2 == 0:
                evensum += new_val - nums[idx]
            
            nums[idx] = new_val
            
            res.append(evensum)
            # print(evensum, nums)
        return res
        