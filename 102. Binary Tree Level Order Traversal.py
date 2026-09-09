# Sep 9, 2026 102-4
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import defaultdict

        # default dict
        level_dic = defaultdict(list)

        # new function: node, level
        def dfs(node, level):
            if not node:
                return
            # add the node to the corresponding level
            level_dic[level].append(node.val)
            # call next level(child node, level + 1)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        res = []
        for key in sorted(level_dic.keys()):
            res.append(level_dic[key])
        return res


# Nov 22, 2023 102-3
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque([])
        if root:
            queue.append(root)
        res = []

        while queue:
            curr_level = []
            for _ in range(len(queue)):

                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                curr_level.append(node.val)
            res.append(curr_level)
        return res


import collections


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        deque = collections.deque([])

        if root:
            deque.append(root)
        res = []

        while deque:
            nodes_in_level = []
            for i in range(len(deque)):
                node = deque.popleft()
                nodes_in_level.append(node.val)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(nodes_in_level)

        return res
