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
#2
import collections
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        queue = collections.deque([])
        res = 0
        for item in nestedList:
            queue.append((item,1))
            while queue:
                popped, depth = queue.popleft()
                if popped.isInteger():
                    res += popped.getInteger()*depth
                else:
                    for it in popped.getList():
                        queue.append((it,depth+1))
        
        return res


import collections
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        queue = collections.deque([])
        res = 0
        for item in nestedList:
            depth = 1
            queue.append((depth, item))
            while queue:
                pop_depth, val = queue.popleft()
                if val.isInteger():
                    res += pop_depth * val.getInteger()
                else:
                    pop_depth += 1
                    for it in val.getList():
                        queue.append((pop_depth, it))
        
        return res