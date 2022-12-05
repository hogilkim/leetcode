from collections import defaultdict
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        curr = defaultdict(int)
        
        i = 0
        while i < len(formula):
            if formula[i] == "(":
                stack.append(copy.deepcopy(curr))
                curr.clear()
                i += 1
            elif formula[i] == ")":
                j = i+1
                
                while j <len(formula) and formula[j].isdigit():
                    j += 1
                
                num = 1 if i+1==j else int(formula[i+1:j])
                
                for key in curr.keys():
                    curr[key] *= num
                
                for key, val in curr.items():
                    stack[-1][key] += val
                curr = stack.pop()
                i = j
            else:
                j = i + 1
                while j < len(formula) and formula[j].islower():
                    j += 1
                
                atom = formula[i:j]
                
                k = j
                while k<len(formula) and formula[k].isdigit():
                    k += 1
                
                num = 1 if j==k else int(formula[j:k])
                curr[atom] += num
                i = k
                
        return "".join([atom+(str(num) if num>1 else "") for atom,num in sorted(curr.items())])