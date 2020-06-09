# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = []
        max_path = 0
        d = {None : -1}
        stack.append(root)
        while(stack):
            curr_node = stack[-1]
            if curr_node.left in d and curr_node.right in d:
                curr_node = stack.pop()
                left = d[curr_node.left] + 1
                right = d[curr_node.right] + 1
                d[curr_node] = max(left, right)
                max_path = max(max_path, left + right)

            else:
                if curr_node.left:
                    stack.append(curr_node.left)
                if curr_node.right:
                    stack.append(curr_node.right)

        return max_path
        
