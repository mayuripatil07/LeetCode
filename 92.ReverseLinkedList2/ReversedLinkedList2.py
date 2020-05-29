# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        count = 0
        curr = head
        prev = None
        while(count < m-1):
            prev = curr
            curr = curr.next
            count += 1

        first = prev
        second = curr
        while(count < n):
            nxt = second.next
            second.next = first
            first = second
            second = nxt
            count += 1

        if prev:
            prev.next = first
        else:
            head = first

        curr.next = second

        return head
            
