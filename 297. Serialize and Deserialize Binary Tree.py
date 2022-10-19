class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        NONE = "#"
        
        preorder = []
        
        def dfs(node):
            if not node:
                preorder.append(NONE)
                return
            
            preorder.append(str(node.val))
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        return ",".join(preorder)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        NONE = "#"
        preorder = data.split(",")
                    
        i = 0
        
        def dfs():
            nonlocal i
            if i >= len(preorder): return None
            if preorder[i] == NONE:
                i += 1
                return None
                
            curr_node = TreeNode(int(preorder[i]))
            i+=1
            
            curr_node.left = dfs()
            curr_node.right = dfs()
    
            return curr_node
        return dfs()


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        # DFS solution (preorder)
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
        
        # Tried BFS, failed
        # if not root:
        #     return "null"
        # bfs_waiting = collections.deque([])
        # bfs_waiting.append(root)
        # string = ""
        # while bfs_waiting:
        #     curr = bfs_waiting.popleft()
        #     if curr:
        #         children = [curr.left, curr.right]
        #         bfs_waiting += children
        #         string += str(curr.val) + " "
        #     else:
        #         string += "null "
        # return string
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # DFS solution (preorder)
        values = data.split(',')
        self.i = 0
        def dfs():
            if values[self.i] == "N":
                self.i += 1
                return None
            new_node = TreeNode(int(values[self.i]))
            self.i += 1
            new_node.left = dfs()
            new_node.right = dfs()
            return new_node
        return dfs()
    
    
    
        # Tried BFS, failed
#         data_list = data.split()
#         root = TreeNode()
        
#         if data_list[0] == "null":
#             return None
        
#         root.val = int(data_list[0])
        
#         bfs_waiting = collections.deque([])
#         bfs_waiting.append(root)
        
#         def make_node(index):
            
#             if index >= len(data_list) or data_list[index] == "null" :
#                 return None
#             else:
#                 new_node = TreeNode()
#                 new_node.val = int(data_list[index])
#                 return new_node
#         i = 0
#         while bfs_waiting:
#             curr = bfs_waiting.popleft()
#             if curr:
#                 left_child_index, right_child_index = 2*(i+1) -1, 2*(i+1)
                
#                 curr.left = make_node(left_child_index)
#                 curr.right = make_node(right_child_index)
#                 bfs_waiting += [curr.left, curr.right]
#             i += 1
#         return root
            
                

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))