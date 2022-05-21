# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.appendLefts(root)
    def next(self) -> int:
        node = self.stack.pop()
        res = node.val
        self.appendLefts(node.right)
        
        return res
        
    def hasNext(self) -> bool:
        return self.stack != []
    
    def appendLefts(self, node):
        while node:
            self.stack.append(node)
            node = node.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()