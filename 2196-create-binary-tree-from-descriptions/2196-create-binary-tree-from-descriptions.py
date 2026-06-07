# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes={}
        seen=set()
        for parent,child,left in descriptions:
            if parent not in nodes:
                nodes[parent]=TreeNode(parent)
            if child not in nodes:
                nodes[child]=TreeNode(child)
            if left:
                nodes[parent].left=nodes[child]
            else:
                nodes[parent].right=nodes[child]
            seen.add(child)
        for val in nodes:
            if val not in seen:
                return nodes[val]