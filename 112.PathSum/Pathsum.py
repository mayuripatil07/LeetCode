# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        stack = []
        stack.append((root, root.val))
        while(stack):
            curr_val, curr_sum = stack.pop()

            if curr_val.left:
                stack.append((curr_val.left, curr_sum + curr_val.left.val))

            if curr_val.right:
                stack.append((curr_val.right, curr_sum + curr_val.right.val))

            if not curr_val.right and not curr_val.left:
                if curr_sum == sum:
                    return True

        return False
                
