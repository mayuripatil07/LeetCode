# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        queue = deque()
        reverse = False
        result = []
        queue.append(root)
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

            if reverse:
                curr_level.reverse()
                result.append(curr_level)
                reverse = False
            else:
                result.append(curr_level)
                reverse = True

        return result
