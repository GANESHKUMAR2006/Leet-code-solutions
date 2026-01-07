# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subsum=[]
        def track(node):
            if not node:
                return 0
            s=node.val+track(node.left)+track(node.right)
            subsum.append(s)
            return s
        total=track(root)
        ans=0
        for s in subsum:
            ans=max(ans,s*(total-s))
        return ans%(10**9+7)