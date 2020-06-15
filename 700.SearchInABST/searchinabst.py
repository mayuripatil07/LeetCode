# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        curr_node = root
        if not curr_node:
            return None
        if curr_node.val == val:
            return curr_node
        if val > curr_node.val:
            return self.searchBST(curr_node.right, val)
        else:
            return self.searchBST(curr_node.left, val)

        return None
