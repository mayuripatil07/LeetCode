"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        hmap = collections.defaultdict(lambda : Node(0))
        hmap[None] = None
        n = head
        while(n):
            hmap[n].val = n.val
            hmap[n].next = hmap[n.next]
            hmap[n].random = hmap[n.random]
            n = n.next
        return hmap[head]
