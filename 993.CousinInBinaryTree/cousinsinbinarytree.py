# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = deque()
        queue.append((root,0,0))
        hmap = collections.defaultdict(list)
        while(queue):
            curr_node, depth, parent = queue.popleft()
            hmap[curr_node.val] = [depth, parent]
            if curr_node.right:
                queue.append((curr_node.right, depth + 1, curr_node.val))

            if curr_node.left:
                queue.append((curr_node.left, depth + 1, curr_node.val))

        if hmap[x][0] == hmap[y][0] and hmap[x][1] != hmap[y][1]:
            return True
        return False

            
