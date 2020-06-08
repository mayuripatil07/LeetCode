# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return None
        stack = []
        result = []
        stack.append((root, str(root.val)))
        while(stack):
            curr, path = stack.pop()
            if not curr.left and not curr.right:
                result.append(path)

            if curr.left:
                stack.append((curr.left, path + "->" + str(curr.left.val)))

            if curr.right:
                stack.append((curr.right, path + "->" + str(curr.right.val)))

        return result
