# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head1 = l1
        head2 = l2
        sum_list = []
        carry = 0
        while(head1 or head2):
            if not head1:
                i = 0
            else:
                i = head1.val
            if not head2:
                j = 0
            else:
                j = head2.val
            s = i + j + carry
            if s >= 10:
                carry = 1
                rem = s % 10
                sum_list.append(rem)
            else:
                carry = 0
                sum_list.append(s)
            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next
        if carry:
            sum_list.append(carry)

        sumlist = ListNode(sum_list.pop(0))
        head = sumlist
        while(sum_list):
            head.next = ListNode(sum_list.pop(0))
            head = head.next
        return sumlist
