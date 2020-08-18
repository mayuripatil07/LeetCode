# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        hmap = collections.defaultdict(list)
        def buildhmap(node, parent):
            if node and parent:
                hmap[node].append(parent)
                hmap[parent].append(node)

            if node.left:
                buildhmap(node.left,node)
            if node.right:
                buildhmap(node.right,node)

        buildhmap(root, None)

        queue = deque()
        queue.append(target)
        visited = set()
        while queue and K > 0:
            for _ in range(len(queue)):
                a = queue.popleft()
                visited.add(a)
                for n in hmap[a]:
                    if n not in visited:
                        queue.append(n)

            K -= 1

        return [ans.val for ans in queue]
