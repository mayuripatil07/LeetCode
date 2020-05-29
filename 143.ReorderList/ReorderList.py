# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        #middle of linkedlist
        slow = head
        fast = head
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        #reverse
        curr = slow
        prev = None
        while(curr):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second = prev
        first = head
        while(second.next):
            nxt = first.next
            first.next = second
            first = nxt

            nxt = second.next
            second.next = first
            second = nxt

        return head
