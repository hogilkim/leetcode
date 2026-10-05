# Oct 5, 2026 416-3
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        mem = set([0])
        target = nums_sum // 2

        for num in nums:
            nextmem = mem.copy()
            for element in mem:
                if element + num == target:
                    return True
                nextmem.add(element + num)
            nextmem.add(num)
            mem = nextmem.copy()
        return False

        # if sum(nums)%2 != 0: return False

        # memo = {}
        # def backtracking(i, num1, num2):
        #     if i == len(nums):
        #         return num1 == num2
        #     if (i, num1, num2) in memo: return memo[(i, num1, num2)]
        #     memo[(i, num1, num2)] = backtracking(i+1, num1+nums[i], num2) or backtracking(i+1, num1, num2+nums[i])
        #     return memo[(i, num1, num2)]

        # return backtracking(0,0,0)


# second attempt - solve again
# Dec 11, 2023 416-2
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for num in nums:
            nextDP = set()
            for val in dp:
                if num + val == target:
                    return True
                nextDP.add(num + val)
                nextDP.add(val)
            dp = nextDP

        return True if target in nextDP else False

        # if sum(nums)%2: return False
        # target = sum(nums)//2

        # memo = {}
        # def backtracking(part, idx):
        #     if part == target: return True
        #     if idx >= len(nums): return False
        #     if (part, idx) in memo: return memo[(part, idx)]

        #     res = False

        #     # include idx
        #     part += nums[idx]
        #     res = res or backtracking(part, idx+1)

        #     # X include idx
        #     part -= nums[idx]
        #     res = res or backtracking(part, idx+1)

        #     memo[(part, idx)] = res

        #     return res

        # return backtracking(0,0)


# solve again
# first attempt - Jan 16, 2022
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums)):
            nextDP = set()

            for val in dp:
                if val + nums[i] == target:
                    return True
                nextDP.add(val + nums[i])
                nextDP.add(val)

            dp = nextDP

        return True if target in dp else False
