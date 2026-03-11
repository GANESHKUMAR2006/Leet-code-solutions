"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        from collections import deque
        if not root:
            return 
        dq=deque([root])
        ans=[]
        while dq:
            level=[]
            for _ in range(len(dq)):
                value=dq.popleft()
                level.append(value.val)
                for child in value.children:
                    if child:
                        dq.append(child)
            ans.append(level)
        return ans