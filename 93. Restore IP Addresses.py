class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12: return []
        
        res = []
                    #starting idx
        def backtracking(idx, part):
            if idx >= len(s) and len(part) >= 4: 
                res.append(".".join(part))
                return
            if idx >= len(s) or len(part) >= 4: return
            
            
            for i in range(idx+1, min(idx+4, len(s)+1)):
                subip = s[idx:i]
                if len(subip)>=2 and subip[0] == '0':
                    break
                if int(subip)>255:
                    break
                backtracking(i, part+[subip])
        backtracking(0,[])
        return res
                