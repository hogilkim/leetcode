# similar to word break
# very hard
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        stickCount = []
        
        # can be replaced to Counter
        
        for i, string in enumerate(stickers):
            stickCount.append({})
            for char in string:
                stickCount[i][char] = 1 + stickCount[i].get(char, 0)
        
        
        # key = subseq of target | val = min num of stickers
        dp={}
        
        def dfs(t, stick):
            if t in dp:
                return dp[t]
            
            res = 1 if stick else 0
            remainT = ""
            for char in t:
                if char in stick and stick[char] > 0:
                    stick[char] -= 1
                else:
                    remainT += char
            if remainT:
                used = float("inf")
                
                for s in stickCount:
                    if remainT[0] not in s:
                        continue
                                                    # s is in dict. so need to copy
                    used = min(used, dfs(remainT, s.copy()))
                dp[remainT] = used
                
                res += used
            return res
        
        res = dfs(target, {})
        return res if res != float("inf") else -1