"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertval: int) -> 'Node':
        if not head:
            newNode =  Node(insertval,None)
            newNode.next = newNode
            return newNode

        curr = head
        while(True):
            if curr.val <= insertval <= curr.next.val:
                break

            elif curr.val > curr.next.val:
                if insertval >= curr.val and insertval >= curr.next.val:
                    break
                elif insertval <= curr.val and insertval <= curr.next.val:
                    break
            curr = curr.next
            if curr == head:
                break

        newNode = Node(insertval)
        temp = curr.next
        curr.next = newNode
        newNode.next = temp
        return head
        
