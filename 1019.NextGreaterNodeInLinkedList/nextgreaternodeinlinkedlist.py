# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        res = []
        temp = head
        index = 0
        while(temp):
            while(stack and stack[-1][0] < temp.val):
                val , i = stack.pop()
                res[i] = temp.val
            res.append(0)
            stack.append((temp.val,index))
            index += 1
            temp = temp.next

        return res
   
