class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        res = []
        
        combs = set()
        for i in range(len(stamp)):
            for j in range(len(stamp)-i):
                combs.add('#'*i + stamp[i:len(stamp)-j] + '#'*j)
        
        # print(combs)
        
        finished = '#'*len(target)
        
        while target!=finished:
            
            found = False
            
            for i in range(len(target)-len(stamp),-1,-1):
                if target[i:i+len(stamp)] in combs:
                    target = target[:i] + '#'*len(stamp) + target[i+len(stamp):]
                    res.append(i)
                    found = True
            if not found: return []
        
        return res[::-1]