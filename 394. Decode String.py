class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        
        currnum = 0
        stack = []
        
        for char in s:
            if char.isdigit():
                currnum = currnum*10 + int(char)
            elif char == "[":
                stack.append(res)
                stack.append(currnum)
                res = ""
                currnum = 0
            elif char == "]":
                num = stack.pop()
                prev_str = stack.pop()
                res = prev_str + res*num
            else:
                res += char
        
        return res

        
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = ""
        
        for c in s:
            if c == "[":
                stack.append(curr_str)
                stack.append(curr_num)
                curr_str = ""
                curr_num = 0
            
            elif c == "]":
                num = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + curr_str * num
            
            elif c.isdigit():
                curr_num = curr_num*10 + int(c)
            
            else:
                curr_str += c
        
        return curr_str