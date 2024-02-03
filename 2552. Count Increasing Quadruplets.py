# Very hard - solve again Feb 3, 2024 2252
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        smaller_than_k = [[0]*len(nums) for _ in range(len(nums))]

        for i in range(1, len(nums)):
            for j in range(0, i+1):
                smaller_than_k[i][j] = smaller_than_k[i][j-1] + int(nums[i] > nums[j])
        res = 0

        greater_than_j = [[0]*len(nums) for _ in range(len(nums))]
        for j in range(len(nums)-2, -1, -1):
            greater_than_j[j][len(nums)-1] = int(nums[j] < nums[len(nums)-1])
            for i in range(len(nums)-2, j-1, -1):
                greater_than_j[j][i] = greater_than_j[j][i+1] + int(nums[j] < nums[i])


        for j in range(1, len(nums)-2):
            for k in range(j+1, len(nums)-1):
                if nums[k] < nums[j]:
                    left = smaller_than_k[k][j]
                    right = greater_than_j[j][k]
                    res += left * right
        
        return res