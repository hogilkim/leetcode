# Oct 6, 2026 785-2
from collections import deque


class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        teams = [0] * n  # -1 or 1

        def bfs(i):
            queue = deque([i])
            teams[i] = 1
            while queue:
                idx = queue.popleft()
                for nei in graph[idx]:
                    if teams[nei] == teams[idx]:
                        return False
                    elif teams[nei] == 0:
                        teams[nei] = -1 * teams[idx]
                        queue.append(nei)
            return True

        for node in range(n):
            if teams[node] == 0:
                if not bfs(node):
                    return False
        return True


from collections import defaultdict


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        graph_dic = defaultdict(list)

        for n, lst in enumerate(graph):
            for adj in lst:
                graph_dic[n].append(adj)

        teams = [set(), set()]

        def dfs(node, team, add):
            teams[team].add(node)

            opponent_team = team + add

            for adj in graph_dic[node]:
                if adj in teams[team]:
                    return False
                elif adj not in teams[opponent_team]:
                    if not dfs(adj, opponent_team, -add):
                        return False

            return True

        for node in range(len(graph)):
            if node not in teams[0] and node not in teams[1]:
                if not dfs(node, 0, 1):
                    return False
        return True
