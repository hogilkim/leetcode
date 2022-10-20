# 헷갈림
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        
        preorder = preorder.split(',')
        
        idx = -1
        
        for s in preorder:
            stack.append(s)
            idx += 1
            while self.endsWithTwoHash(stack, idx):
                # pop hash signs
                stack.pop()
                stack.pop()
                idx -= 2
                if idx <0: return False
                
                # pop value
                stack.pop()
                
                stack.append("#")
        
        if len(stack) == 1 and stack[0] == "#": return True
        return False
        
        
        
        
    
    
    def endsWithTwoHash(self,stack, idx):
        if idx < 1: return False
        
        if stack[idx] =="#" and stack[idx-1] == "#":
            return True
        return False
            
            


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