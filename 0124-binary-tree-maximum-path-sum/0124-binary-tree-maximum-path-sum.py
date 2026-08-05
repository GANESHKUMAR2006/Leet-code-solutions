# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=float('-inf')
        def dfs(node):
            nonlocal ans
            if node==None:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            all=node.val+left+right
            maxleft=max(node.val,node.val+left)
            maxright=max(node.val,node.val+right)
            oneside=max(maxright,maxleft)
            final=max(oneside,all)
            ans=max(ans,final)
            return oneside
        dfs(root)
        return ans