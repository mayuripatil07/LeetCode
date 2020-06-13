# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = deque()
        result = []
        queue.append(root)
        while(queue):
            n = len(queue)
            curr_level = []
            while(n):
                curr = queue.popleft()
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)

                curr_level.append(curr.val)
                n -= 1

            result.append(max(curr_level))

        return result
