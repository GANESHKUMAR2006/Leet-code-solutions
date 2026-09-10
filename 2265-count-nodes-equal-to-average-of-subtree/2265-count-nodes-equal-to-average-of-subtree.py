# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count=0
        def dfs(node):
            if not node:
                return 0,0
            left,lcount=dfs(node.left)
            right,rcount=dfs(node.right)
            total=left+right+node.val
            totalcount=lcount+rcount+1
            avg=total//totalcount
            if node.val==avg:
                self.count+=1
            return total,totalcount

        dfs(root)
        return self.count
