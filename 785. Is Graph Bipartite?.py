from collections import defaultdict
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        graph_dic = defaultdict(list)
        
        for n, lst in enumerate(graph):
            for adj in lst:
                graph_dic[n].append(adj)
        
        teams = [set(),set()]
        
        def dfs(node, team, add):            
            teams[team].add(node)
            
            opponent_team = team + add
            
            for adj in graph_dic[node]:
                if adj in teams[team]: return False
                elif adj not in teams[opponent_team]: 
                    if not dfs(adj, opponent_team, -add): return False
            
            return True
        
        
        for node in range(len(graph)):
            if node not in teams[0] and node not in teams[1]:
                if not dfs(node, 0,1): return False
        return True