class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0:-1}
        
        modsum = 0
        
        for idx, num in enumerate(nums):
            modsum = (modsum + num)%k
            
            if modsum not in dic:
                dic[modsum] = idx
                
            elif idx - dic[modsum] >= 2:
                return True
        
        return False