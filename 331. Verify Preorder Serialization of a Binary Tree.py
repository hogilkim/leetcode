from collections import deque
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        node_list = preorder.split(",")
        slot = 1
        
        for node in node_list:
            if slot <=0: return False
            if node == "#": slot -= 1
            else: slot += 1
        
        return not slot
        
        
        
        # wrong
#         node_list = deque(preorder.split(","))
        
#         def dfs():
#             if not node_list: return True
#             val = node_list.popleft()
#             if val == "#": return True
#             if len(node_list) < 2: return False
            
#             if node_list[0] == node_list[1] == "#":
#                 node_list.popleft(); node_list.popleft();
            
#             return dfs() and dfs()
        
#         return dfs() and not node_list