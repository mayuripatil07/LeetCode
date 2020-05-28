# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        curr = head
        count = 0
        while(curr):
            count += 1
            prev = curr
            curr = curr.next

        prev.next = head
        curr = head
        s = (count-k) % count
        while(s):
            prev = curr
            curr = curr.next
            s -= 1
        prev.next = None
        return curr
        
