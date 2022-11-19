class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross_prod(p1,p2,p3):
            a = p3[0]-p2[0]
            b = p3[1]-p2[1]
            c = p2[0]-p1[0]
            d = p2[1]-p1[1]
            
            return a*d-b*c
        
        def counterclockwisePoints(points):
            stack = []
            
            for p in points:
                while len(stack)>=2 and cross_prod(stack[-2],stack[-1], p)>0:
                    stack.pop()
                stack.append(tuple(p))
            
            return stack
        
        
        trees = sorted(trees, key = lambda x:(x[0],x[1]))
        
        leftToRight = counterclockwisePoints(trees)
        rightToLeft = counterclockwisePoints(trees[::-1])
        
        return list(set(leftToRight+rightToLeft))