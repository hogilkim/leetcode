class Solution:
    def tree2str(self, root: Optional[TreeNode], string = "") -> str:
        string = str(root.val)
        
        if root.left:
            string += "(" + self.tree2str(root.left, string) + ")"
        if root.right:
            if not root.left: string += "()"
            string += "(" + self.tree2str(root.right, string) + ")"
        
        return string