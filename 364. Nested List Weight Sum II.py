# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
import collections
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        depth_dic = collections.defaultdict(list)
        
        max_depth = 1
        
        queue = collections.deque([])
        
        for element in nestedList:
            queue.append((element, 1))
            
            while queue:
                items, depth = queue.popleft()
                
                if items.isInteger():
                    depth_dic[depth].append(items.getInteger())
                else:
                    for item in items.getList():
                        queue.append((item, depth + 1))
                    max_depth = max(max_depth, depth+1)
        
        res = 0
        print(depth_dic)
        for key, val in depth_dic.items():
            for integer in val:
                res += (max_depth - key + 1)*integer
        
        return res
            
        
        
        
        
        
        
        