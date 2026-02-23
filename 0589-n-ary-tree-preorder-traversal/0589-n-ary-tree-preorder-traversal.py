"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return 
        arr=[]
        arr.append(root.val)
        def traverse(node):
            for i in node.children:
                arr.append(i.val)
                traverse(i)
        traverse(root)
        return arr