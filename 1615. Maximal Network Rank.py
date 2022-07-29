import collections
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        network = collections.defaultdict(list)
                
        for i,j in roads:
            network[i].append(j)
            network[j].append(i)
        
        checked = set()
        max_rank = 0
        for i in range(n):
            for j in range(n):
                if i==j: continue
                if (i,j) in checked: continue
                curr = len(network[i]) + len(network[j])
                if j in network[i]: curr -= 1
                max_rank = max(max_rank, curr)
                checked.add((j,i))
        
        return max_rank