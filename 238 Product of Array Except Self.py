# Third attempt - solve again
# Dec 1, 2023 238-3

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)

        prod_from_left = 1
        prod_from_right = 1

        for i in range(len(nums)):
            res[i] *= prod_from_left
            prod_from_left *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            res [i] *= prod_from_right
            prod_from_right *= nums[i]
        
        return res


# second attempt Dec 28, 2021 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        zero_num = 0
        
        for num in nums:
            if num != 0:
                mult *=num
            else:
                zero_num += 1
        
        result = []
        for num in nums:
            if zero_num > 0:
                if num == 0 and zero_num < 2:
                    result.append(mult)
                else:
                    result.append(0)
            else:
                result.append(int(mult/num))
        
        return result

# class Solution(object):
#     def productExceptSelf(self, nums):
        

        # all_multiple = 1
        # zero_num = 0
        # for num in nums:
        #     if num != 0:
        #         all_multiple *= num
        #     else:
        #         zero_num += 1
                
                
        # return_list = []        
        
        # if zero_num > 1:
        #     return [0 for i in range(len(nums))]
        # elif zero_num == 1:
        #     return_list = [0 for i in range(len(nums))]
        #     return_list[nums.index(0)] = all_multiple
        #     return return_list
        
        # for num in nums:
        #     return_list.append(all_multiple/num)
        # return return_list
        