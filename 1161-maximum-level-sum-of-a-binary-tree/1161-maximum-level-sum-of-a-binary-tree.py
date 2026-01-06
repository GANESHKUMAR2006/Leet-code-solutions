# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxsum=float('-inf')
        level=1
        ans=1
        from collections import deque
        dq=deque([root])
        while dq:
            levelsum=0
            size=len(dq)
            for _ in range(size):
                node=dq.popleft()
                levelsum+=node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            if maxsum<levelsum:
                maxsum=levelsum
                ans=level
            level+=1
        return ans