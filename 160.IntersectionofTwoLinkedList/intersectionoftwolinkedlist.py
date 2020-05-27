class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curr, curr1 = headA, headB
        while(curr1 != curr):
            if curr:
                curr = curr.next
            else:
                curr = headB
            if curr1:
                curr1 = curr1.next
            else:
                curr1 = headA

        return curr
                
