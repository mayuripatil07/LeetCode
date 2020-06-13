# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = []
        s = str(root.val)
        stack.append((root, s))
        result = []
        while(stack):
            curr, path = stack.pop()
            if not curr.right and not curr.left:
                result.append(int(path))
            if curr.right:
                stack.append((curr.right, path + str(curr.right.val)))
            if curr.left:
                stack.append((curr.left, path + str(curr.left.val)))

        return sum(result)
