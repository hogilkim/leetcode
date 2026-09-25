# Sep 25, 2026 230-3
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        res = 0

        def dfs(node, seq, k):
            nonlocal res

            cumul = seq
            if node.left:
                cumul = dfs(node.left, cumul, k)
            cumul += 1
            if cumul == k:
                res = node.val

            if node.right:
                cumul = dfs(node.right, cumul, k)

            return cumul

        dfs(root, 0, k)
        return res


# Dec 20, 2023 230-2
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = -1

        def dfs(node, acc):
            nonlocal res
            if not node:
                return 0

            left = dfs(node.left, acc)
            if left + acc + 1 == k:
                res = node.val
            right = dfs(node.right, left + acc + 1)

            return left + 1 + right

        dfs(root, 0)
        return res


# solve again
# second attempt - Jan 13, 2022
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        n = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        return sorted(self.helper(root, []))[k - 1]

    def helper(self, node, num_list):
        if node:
            num_list.append(node.val)
            if node.left:
                num_list += self.helper(node.left, [])
            if node.right:
                num_list += self.helper(node.right, [])
        return num_list
