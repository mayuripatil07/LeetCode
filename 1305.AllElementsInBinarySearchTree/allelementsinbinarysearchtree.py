# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        Tree1 = []
        Tree2 = []
        queue1 = deque()
        if root1:
            queue1.append(root1)
        queue2 = deque()
        if root2:
            queue2.append(root2)
        while(queue1):
            n = len(queue1)
            while(n):
                curr_node = queue1.popleft()
                Tree1.append(curr_node.val)
                if curr_node.left:
                    queue1.append(curr_node.left)
                if curr_node.right:
                    queue1.append(curr_node.right)
                n -= 1

        while(queue2):
            n = len(queue2)
            while(n):
                curr_node = queue2.popleft()
                Tree2.append(curr_node.val)
                if curr_node.left:
                    queue2.append(curr_node.left)
                if curr_node.right:
                    queue2.append(curr_node.right)
                n -= 1

        Tree1 = Tree1 + Tree2
        Tree1.sort()
        return Tree1
