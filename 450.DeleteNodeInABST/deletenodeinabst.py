# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            else:
                temp = root.right
                value = temp.val
                while(temp.left):
                    temp = temp.left
                    value = temp.val
                root.val = value
                root.right = self.deleteNode(root.right, value)
        return root
