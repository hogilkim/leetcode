from collections import defaultdict
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        M, N = len(nums1), len(nums2)
        
        dp = [ [0]*M for _ in range(N) ]
        
        for i in range(M):
            if nums1[i] == nums2[0]:
                dp[0][i] = 1
        for n in range(1, N):
            for m in range(M):
                if m == 0 and nums2[n] == nums1[m]: dp[n][0] = 1
                elif nums2[n] == nums1[m]:
                    dp[n][m] = dp[n-1][m-1] + 1
        return max(max(line) for line in dp)
                