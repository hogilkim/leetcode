class Node:
    def __init__(self, start, end):
        self.total = 0
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class NumArray:

    def __init__(self, nums: List[int]):
        def createBIT(l,r):
            if l>r: return None
            # leaf
            if l == r:
                node = Node(l,r)
                node.total = nums[l]
                return node
            
            # Subtree Root
            mid = (l+r)//2
            
            root = Node(l,r)
            root.left = createBIT(l, mid)
            root.right = createBIT(mid+1, r)
            root.total = root.left.total + root.right.total
            return root
        
        self.treeroot = createBIT(0,len(nums)-1)
            

    def update(self, index: int, val: int) -> None:
        def updateVal(node, idx, val):
            # update leaf
            if node.start == node.end:
                if idx == node.start:
                    node.total = val
                return val
            
            # call recursive
            mid = (node.start +node.end)//2
            if idx <= mid:
                updateVal(node.left, idx, val)
            else:
                updateVal(node.right, idx, val)
            
            # update total
            node.total = node.left.total + node.right.total
            return node
        
        updateVal(self.treeroot, index, val)
            

    def sumRange(self, left: int, right: int) -> int:
        def rangeSum(node, l,r):
            if node.start == l and node.end == r:
                return node.total
            
            mid = (node.start+node.end)//2
            
            if r<=mid:
                return rangeSum(node.left, l, r)
            elif mid+1<=l:
                return rangeSum(node.right, l,r)
            else:
                return rangeSum(node.left, l, mid) + rangeSum(node.right, mid+1, r)
        
        return rangeSum(self.treeroot, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)