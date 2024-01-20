# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solve again Jan 20, 2024 919

from collections import deque
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        nodes_queue = deque([root])
        self.queue = deque([])

        while nodes_queue:
            node = nodes_queue.popleft()
            if not node.left or not node.right:
                self.queue.append(node)
            if node.left:
                nodes_queue.append(node.left)
            if node.right:
                nodes_queue.append(node.right)

    def insert(self, val: int) -> int:
        new_node = TreeNode(val)
        parent = self.queue[0]
        if not parent.left: parent.left = new_node
        else:
            parent.right = new_node
            self.queue.popleft()
        
        self.queue.append(new_node)
        
        return parent.val
        


    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()