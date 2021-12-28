class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i=0
        s_processed = []
        while i < len(s):
            if s[i] == "#":
                if s_processed:
                    s_processed.pop()
            else:
                s_processed += s[i]
            i += 1
        
        j=0
        t_processed = []
        while j < len(t):
            if t[j] == "#":
                if t_processed:
                    t_processed.pop()
            else:
                t_processed += t[j]
            j += 1
        return s_processed == t_processed