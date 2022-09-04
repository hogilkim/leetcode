import collections
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        
        
        def dfs(node, vertical_line, level):
            if not node: return
            dic[vertical_line].append((node.val, level))
            
            dfs(node.left, vertical_line-1, level+1)
            dfs(node.right, vertical_line+1, level+1)
            
            
        dfs(root, 0, 0)
        
        res = []
        
        for key in sorted(dic.keys()):
            
            res.append( [ x[0] for x in sorted(dic[key], key=lambda x: (x[1], x[0])) ] )
        
        
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        
        def dfs(node,vertical_line, level):
            if not node: return
            
            dic[vertical_line].append((node.val, level))
            dfs(node.left, vertical_line-1, level + 1)
            dfs(node.right, vertical_line + 1, level + 1)
            
            
        
        dfs(root,0,0)
        
        res = []
        
        for key in sorted(dic.keys()):
            
            # vals = dic[key]
            # sub_res = []
            # vals = sorted(vals, key=lambda x:x[0])
            # vals = sorted(vals, key=lambda x:x[1])
            # for val in vals:
            #     sub_res.append(val[0])
            # res.append(sub_res)
            
            res.append( [ x[0] for x in sorted(dic[key], key=lambda x:(x[1], x[0]) ) ] )
        
        return res
            