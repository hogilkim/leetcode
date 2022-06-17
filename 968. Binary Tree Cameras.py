# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        cameras = 0
        
        
        # return val: camera, monitored T/F
        def dfs(node):
            nonlocal cameras
            
            if not node:
                return False, True
            
            cam_left, mon_left = dfs(node.left)
            cam_right, mon_right = dfs(node.right)
            
            camera, monitored = False, False
            
            if cam_left or cam_right:
                monitored = True
            if not mon_left or not mon_right:
                camera = True
                cameras+=1
                monitored = True
            
            return camera, monitored
        
        camera, monitored = dfs(root)
        if not monitored: return cameras+1
        return cameras