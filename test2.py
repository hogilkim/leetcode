# validate bst
#           5
#       4
#   3
# 2
# 98


def function(root):

    # dfs (node, min_possible_val, max_poss_val)
    def dfs(node, min_pos_val, max_pos_val):
        # if not node, return
        if not node:
            return True
        # check if the current node is in range
        # if not, update variable to false

        # res = True
        # if not (min_pos_val < node.val < max_pos_val):
        #     res = False
        # # left
        # # dfs to left node, min_possible_val, node.val
        # leftres = dfs(node.left, min_pos_val, node.val)
        # # right
        # # dfs to right, node.val, max_poss_val
        # rightres = dfs(node.right, node.val, max_pos_val)

        # return res and leftres and rightres

        return (
            min_pos_val < node.val < max_pos_val
            and dfs(node.left, min_pos_val, node.val)
            and dfs(node.right, node.val, max_pos_val)
        )

    # call dfs
    return dfs(root, float("-inf"), float("inf"))
    # return res
