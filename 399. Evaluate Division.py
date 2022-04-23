import collections
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        eq_dic = collections.defaultdict(list)
        
        for i in range(len(equations)):
            eq_dic[equations[i][0]].append((equations[i][1], values[i]))
            eq_dic[equations[i][1]].append((equations[i][0], 1/values[i]))
            
        res = []
        

        
        path = set()
        
        def dfs(target, curr_var, val):
            
            # if curr_var in path: return val
            
            path.add(curr_var)
            
            ans = -1
            
            for var,coeff in eq_dic[curr_var]:
                # print(target, var, coeff)
                if var == target:
                    ans = coeff*val
                    break
                elif var not in path:
                    temp = dfs(target, var, val*coeff)
                    if temp>0:
                        ans = temp
                        break
                                                
            path.remove(curr_var)
            
            return ans

        for x,y in queries:
            if x not in eq_dic or y not in eq_dic:
                res.append(-1)
            elif x==y: res.append(1)
            else:
                res.append(dfs(y, x, 1))
        
        return res
                