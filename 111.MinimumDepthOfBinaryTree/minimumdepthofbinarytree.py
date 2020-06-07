# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = deque()
        queue.append(root)
        count = 0
        while(queue):
            count += 1
            n = len(queue)
            for i in range(n):
                curr_val = queue.popleft()
                if not curr_val.left and not curr_val.right:
                    return count

                if curr_val.left:
                    queue.append(curr_val.left)

                if curr_val.right:
                    queue.append(curr_val.right)
