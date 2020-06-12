# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        queue = deque()
        queue.append(root)
        parent = collections.defaultdict(list)
        while(queue):
            n = len(queue)
            curr_level  = []
            while(n):
                curr_node = queue.popleft()
                if curr_node.left:
                    queue.append(curr_node.left)
                    parent[curr_node.left] = curr_node
                if curr_node.right:
                    queue.append(curr_node.right)
                    parent[curr_node.right] = curr_node

                curr_level.append(curr_node)
                n -= 1

        while(len(curr_level) > 1):
            s = set()
            for node in curr_level:
                s.add(parent[node])
            curr_level = list(s)

        return curr_level[0]
