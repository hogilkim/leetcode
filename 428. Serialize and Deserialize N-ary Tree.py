

import collections

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        serial = []

        def preorder(node):

            if not node:
                return

            serial.append(str(node.val))

            for child in node.children:
                preorder(child)

            serial.append("#")      # indicates no more children, continue serialization from parent

        preorder(root)
        return " ".join(serial)
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        queue = collections.deque(data.split())
        root = Node(int(queue.popleft()), [])
        
        def dfs(node):
            while queue[0] != '#':
                child = Node(int(queue.popleft()),[])
                node.children.append(child)
                dfs(child)
            queue.popleft()
            
            return node
        
        dfs(root)
        return root

                

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))