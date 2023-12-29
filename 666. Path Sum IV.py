# Dec 29, 2023 666
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        tree = {}
        for num in nums:
            depth = int(str(num)[0])
            position = int(str(num)[1])
            val = int(str(num)[2])

            tree[(depth, position)] = val

        total_val = 0
        
        def dfs(depth, pos, pathval):
            nonlocal total_val
            left = (depth+1, pos*2-1)
            right = (depth+1, pos*2)

            pathval += tree[(depth, pos)]

            if left not in tree and right not in tree:
                total_val += pathval
                return
            
            if left in tree: dfs(left[0],left[1], pathval)
            if right in tree: dfs(right[0], right[1], pathval)
        
        dfs(1,1,0)

        return total_val