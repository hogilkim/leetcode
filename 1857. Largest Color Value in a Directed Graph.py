import collections
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # discussion solution
        graph = collections.defaultdict(list)
        incoming = [0 for i in range(len(colors))]
        for i,j in edges:
            graph[i].append(j)
            incoming[j] += 1
        stack = [node for node in range(len(colors)) if incoming[node] == 0]
        
        color_counts = [[0]*26 for _ in range(len(colors))]
        
        
        while stack:
            node = stack.pop()
            color_counts[node][ord(colors[node]) - ord('a')]+= 1
            
            for nei in graph[node]:
                color_counts[nei] = list(map(max, color_counts[node], color_counts[nei]))
                incoming[nei] -= 1
                if incoming[nei] == 0: stack.append(nei)
        
        return -1 if sum(incoming) > 0 else max( [max(color_counts[node]) for node in \
                                                 range(len(colors))] )
        
        # my solution, TLE
#         graph = collections.defaultdict(list)
#         incoming = [0 for i in range(len(colors))]
#         for i,j in edges:
#             graph[i].append(j)
#             incoming[j] += 1
        
#         starting_points = [node for node in range(len(colors)) if incoming[node] == 0]
#         if not starting_points: return -1
        
        
#         path = set()
        
#         max_freq = 0
#         color_counter = collections.defaultdict(int)

        
#         def dfs(node):
#             nonlocal max_freq
            
#             if node in path: return -1
#             path.add(node)
            
#             color_counter[colors[node]] += 1
            
#             max_freq = max(max_freq, max(color_counter.values()))
            
#             for nei in graph[node]:
#                 if dfs(nei) == -1:
#                     return -1
                
#             color_counter[colors[node]] -= 1
#             path.remove(node)
            
#             return 1
                
        
#         for node in starting_points:
#             if dfs(node) == -1: return -1
            
        
        
        
#         return max_freq