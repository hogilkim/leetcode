import collections
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9+7
        
        c = collections.Counter(arr)
        keys = sorted(c.keys())
        res = 0
        for i, num1 in enumerate(keys):
            j, k = i, len(keys)-1
            
            while j<=k:
                num2, num3 = keys[j], keys[k]
                if num1+num2+num3 < target:
                    j += 1
                elif num1+num2+num3 > target:
                    k -= 1
                else:
                    if i==j<k:
                        res += c[num1]*(c[num2]-1)//2*c[num3]
                    elif i<j==k:
                        res += c[num1]*c[num2]*(c[num3]-1)//2
                    elif i<j<k:
                        res += c[num1]*c[num2]*c[num3]
                    else:
                        res += c[num1]*(c[num2]-1)*(c[num3]-2)//6
                    j+=1
                    k-=1
        
        return res%MOD