# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        result = []
        while(queue):
            n = len(queue)
            curr_level = []
            while(n):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                curr_level.append(curr.val)
                n -= 1

            result.append(curr_level[-1])

        return result
       
