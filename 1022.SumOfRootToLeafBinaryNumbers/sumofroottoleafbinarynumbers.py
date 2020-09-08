# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        stack = []
        result = []
        s = 0
        stack.append((root, str(root.val)))
        while(stack):
            curr_node, curr_val = stack.pop()
            if curr_node.left:
                curr_val_left= ""
                curr_val_left = curr_val + str(curr_node.left.val)
                stack.append((curr_node.left, curr_val_left))
            if curr_node.right:
                curr_val_right = ""
                curr_val_right =  curr_val + str(curr_node.right.val)
                stack.append((curr_node.right, curr_val_right))
            if not curr_node.right and not curr_node.left:
                result.append(curr_val)
        for i in result:
            s += int(i,2)
        return s
        
