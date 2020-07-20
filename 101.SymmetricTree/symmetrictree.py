# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root.left, root.right)]
        while(stack):
            node1, node2 = stack.pop()
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                stack.append((node1.left, node2.right))
                stack.append((node1.right, node2.left))
            else:
                if node1 == node2:
                    continue
                else:
                    return False
        return True
