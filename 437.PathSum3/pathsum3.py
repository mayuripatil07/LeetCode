# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return 0

        result = 0

        stack = [(root, root.val, [root.val])]

        while(stack):
            curr_node , curr_sum , curr_path = stack.pop()

            if curr_sum == sum:
                result += 1

            temp = curr_sum
            for i in range(len(curr_path)-1):
                temp -= curr_path[i]
                if temp == sum:
                    result += 1

            if curr_node.right:
                stack.append((curr_node.right, curr_sum + curr_node.right.val, curr_path + [curr_node.right.val]))

            if curr_node.left:
                stack.append((curr_node.left, curr_sum + curr_node.left.val, curr_path + [curr_node.left.val]))
        return result
