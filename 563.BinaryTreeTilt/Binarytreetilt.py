# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = []
        stack = []
        stack.append(root)
        d = {None : 0}
        while(stack):
            curr = stack[-1]
            if curr.left in d and curr.right in d:
                curr = stack.pop()
                if curr.left is None and curr.right is None:
                    d[curr] = 0 + 0 + curr.val
                else:
                    left = d[curr.left]
                    right = d[curr.right]
                    d[curr] = left  + right + curr.val
                    diff = abs(left - right)
                    result.append(diff)
            else:
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)


        return sum(result)
                    
