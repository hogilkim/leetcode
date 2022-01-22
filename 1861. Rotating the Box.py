class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        ROW, COL = len(box), len(box[0])
        
        for box_row in box:
            stones_count = 0
            #fast, slow = COL - 1
            stack_ptr = COL - 1
            for i in range(COL-1, -1, -1):
                if box_row[i] == "#":
                    stones_count += 1
                if box_row[i] == "*":
                    while i < stack_ptr:
                        if stones_count:
                            box_row[stack_ptr] = "#"
                            stones_count -= 1
                        else:
                            box_row[stack_ptr] = "."
                        stack_ptr -= 1
                        
                    stack_ptr = i-1
                    
                elif i == 0:
                    while stack_ptr >= 0:
                        if stones_count:
                            box_row[stack_ptr] = "#"
                            stones_count -= 1
                        else:
                            box_row[stack_ptr] = "."
                        
                        stack_ptr -= 1
        
        new_box = [[] for i in range(COL)]
        for row in range(ROW-1, -1, -1):
            
            for col in range(COL):
                new_box[col].append(box[row][col])
        
        
        return new_box