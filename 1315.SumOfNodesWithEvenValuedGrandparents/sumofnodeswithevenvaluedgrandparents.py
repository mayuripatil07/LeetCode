# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        stack = []
        stack.append((root, False))
        result = 0
        while(stack):
            curr, if_sum = stack.pop()
            if if_sum == False:
                if curr.val % 2 == 0:
                    if curr.right:
                        stack.append((curr.right, True))
                    if curr.left:
                        stack.append((curr.left, True))
                else:
                    if curr.right:
                        stack.append((curr.right, False))
                    if curr.left:
                        stack.append((curr.left, False))

            elif if_sum == True:
                if curr.val % 2 == 0:
                    if curr.right:
                        stack.append((curr.right, True))
                        result += curr.right.val
                    if curr.left:
                        stack.append((curr.left, True))
                        result += curr.left.val
                else:
                    if curr.right:
                        stack.append((curr.right, False))
                        result += curr.right.val
                    if curr.left:
                        stack.append((curr.left, False))
                        result += curr.left.val

        return result
