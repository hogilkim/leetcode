class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1]*(n+1)
        
        for node_num in range(2, n+1):
            total_tree_num = 0
            for root in range(1, node_num+1):
                left = root-1
                right = node_num - root
                total_tree_num += dp[left]*dp[right]
            dp[node_num] = total_tree_num
        
        return dp[-1]