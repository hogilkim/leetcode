import collections
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dom_dic = collections.defaultdict(int)
        
        for s in cpdomains:
            num, domain = s.split(" ")
            
            sub_domains = domain.split(".")
            
            idx = len(sub_domains)-1
            while idx >= 0:
                dom_dic[tuple(sub_domains[idx:])] += int(num)
                idx -= 1
                
        res =[]
        
        for key,val in dom_dic.items():
            subd = ".".join(list(key))
            res.append(str(val)+" " + subd)
        
        return res