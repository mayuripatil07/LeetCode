# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        #middle of linkedlist
        slow = head
        fast = head
        while(fast and fast.next):
            prev = slow
            slow = slow.next
            fast = fast.next.next

        #reverse linkedlist
        curr = slow
        prev = None
        while(curr):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        #checking if the nodes are same
        first = head
        second = prev
        while(first.next):
            if first.val == second.val:
                first = first.next
                second = second.next

            else:
                return False
        return True
            
