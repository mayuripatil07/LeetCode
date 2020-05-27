class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2
        s = None

        if not p:
            return q
        if not q:
            return p

        if p.val <= q.val:
            s = p
            p = s.next
        else:
            s = q
            q = s.next

        new_head = s

        while p and q:
            if p.val <= q.val:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p

        return new_head
                
