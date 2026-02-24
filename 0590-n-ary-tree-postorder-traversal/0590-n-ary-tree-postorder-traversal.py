"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans=[]
        if not root:
            return 
        def traversal(root):
            if not root:
                return
            for node in root.children:
                traversal(node)
                ans.append(node.val)
        traversal(root)
        ans.append(root.val)
        return ans