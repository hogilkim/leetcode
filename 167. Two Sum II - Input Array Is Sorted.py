class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # key = subtracted val = idx
        dic = {}
        
        for idx, num in enumerate(numbers):
            if num in dic:
                return [dic[num]+1, idx+1]
            subtracted = target - num
            dic[subtracted] = idx        