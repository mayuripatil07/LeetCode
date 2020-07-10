# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyNode = ListNode(0)
        dummyNode.next = head
        first = dummyNode
        second = dummyNode
        i = 0
        while(i < n+1):
            first = first.next
            i += 1

        while(first):
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummyNode.next



            
