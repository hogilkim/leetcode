class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = "L" + dominoes + "R"
        prev_idx = 0
        ans = ""
        
        for i in range(1, len(dominoes)):
            dom_num = i - prev_idx - 1
            if dominoes[i] == ".": continue
                
            if dominoes[i] == dominoes[prev_idx]:
                ans += dominoes[i] * dom_num
            elif dominoes[i] == "L" and dominoes[prev_idx] == "R":
                m, d = divmod(dom_num, 2)
                ans += "R"*m + "."*d + "L"*m
            else:
                ans += "." * dom_num
                
            
            prev_idx = i
            ans += dominoes[i]
        
        return ans[:-1]
            
            
        