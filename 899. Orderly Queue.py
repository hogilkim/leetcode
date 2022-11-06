class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        lexi_min = s
        if k>1:
            lexi_min = "".join(sorted(list(s)))
        else:
            for i in range(len(s)):
                lexi_min = min(lexi_min, s[i:]+s[:i])
        
        return lexi_min