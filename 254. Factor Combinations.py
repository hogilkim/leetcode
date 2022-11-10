# second try Nov 9 Not prefect

import math
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        
        def dfs(path, divstart, target):
            if len(path)>0: res.append(path+[target])
            
            
            for div in range(divstart, int(math.sqrt(target)+1)):
                if target%div == 0:
                    dfs(path+[div], div, target//div)
        
        
        dfs([],2,n)
        return res

import math
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        if n == 1: return []
        
        def dfs(path, div_start, target):
            if len(path)>0:
                res.append(path+[target])
            
            for div in range(div_start, int(math.sqrt(target)) + 1):
                if target%div == 0:
                    dfs(path+[div], div, target//div)
        
        dfs([],2,n)
        return res