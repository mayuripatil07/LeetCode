# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans = []
        if not root:
            return sum(ans)

        def checkleft(root):
            if root.left:
                if not root.left.left and not root.left.right:
                    ans.append(root.left.val)
                checkleft(root.left)

            if root.right:
                checkleft(root.right)

        checkleft(root)
        return sum(ans)
