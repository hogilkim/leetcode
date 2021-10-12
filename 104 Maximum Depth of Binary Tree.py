# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        depth = traverse(root, 0)
        return depth

        
def traverse (object, depth):
    if object == None:
        return depth
    left_node = object.left
    right_node = object.right
    return max(traverse(left_node, depth+1), traverse(right_node, depth+1))
        
        