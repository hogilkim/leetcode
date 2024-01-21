# solve again Jan 21, 2024 465-2
from collections import defaultdict
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        trans = defaultdict(int)
        for sender, receiver, amount in transactions:
            trans[sender] -= amount
            trans[receiver] += amount

        balance = [value for value in trans.values() if value != 0]
        
        def backtracking(idx, balance):
            if idx == len(balance): return 0
            if balance[idx] == 0: return backtracking(idx+1, balance.copy())

            mintrans = float('inf')
            
            for i in range(idx+1, len(balance)):
                # multiply should be negative
                if balance[i] * balance[idx] < 0:
                    # adjust balance
                    balance[i] += balance[idx]
                    # call backtracking, which return minimum transactions
                    mintrans = min(mintrans, backtracking(idx+1, balance.copy()) + 1 )
                    # revert balance
                    balance[i] -= balance[idx]
            
            return mintrans

        return backtracking(0, balance.copy())

from collections import defaultdict
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        trans = defaultdict(int)
        
        for sender, receiver, amount in transactions:
            trans[receiver] += amount
            trans[sender] -= amount
        
        balance = [value for value in trans.values() if value]
        print(balance)
        
        def dfs(idx, balance_copy):
            if idx == len(balance_copy): return 0
            
            if balance_copy[idx] == 0: return dfs(idx+1, balance_copy.copy())
                
            transnum_min = float('inf')
            
            for i in range(idx+1, len(balance_copy)):
                if balance_copy[i] * balance_copy[idx] < 0:
                    balance_copy[i] += balance_copy[idx]
                    transnum_min = min( transnum_min, dfs(idx+1, balance_copy.copy()) + 1 )
                    
                    if balance_copy[i] == 0: break
                    balance_copy[i] -= balance_copy[idx]
                    
                    
            
            return transnum_min
        
        return dfs(0, balance.copy())
                