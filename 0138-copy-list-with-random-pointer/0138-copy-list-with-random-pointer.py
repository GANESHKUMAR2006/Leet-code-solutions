"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        mp={}
        cur=head
        while cur:
            mp[cur]=Node(cur.val)
            cur=cur.next
        cur=head
        while cur:
            new=mp[cur]
            new.next=mp.get(cur.next)
            new.random=mp.get(cur.random)
            cur=cur.next
        return mp[head]