# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, None, 0)]
        max_length = 0
        while(stack):
            curr, direction, length = stack.pop()
            max_length = max(max_length, length)
            if direction == None:
                if curr.right:
                    stack.append((curr.right, "r", length + 1))
                if curr.left:
                    stack.append((curr.left, "l", length + 1))

            elif direction == "r":
                if curr.right:
                    stack.append((curr.right, "r", 1))
                if curr.left:
                    stack.append((curr.left, "l", length + 1))

            elif direction == "l":
                if curr.right:
                    stack.append((curr.right, "r", length + 1))
                if curr.left:
                    stack.append((curr.left, "l", 1))

        return max_length
