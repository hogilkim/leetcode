class Solution(object):
    def productExceptSelf(self, nums):
        all_multiple = 1
        zero_num = 0
        for num in nums:
            if num != 0:
                all_multiple *= num
            else:
                zero_num += 1
                
                
        return_list = []        
        
        if zero_num > 1:
            return [0 for i in range(len(nums))]
        elif zero_num == 1:
            return_list = [0 for i in range(len(nums))]
            return_list[nums.index(0)] = all_multiple
            return return_list
        
        for num in nums:
            return_list.append(all_multiple/num)
        return return_list
        