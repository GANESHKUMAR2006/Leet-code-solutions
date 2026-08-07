# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return []
        q=deque([root])
        order=1
        while q:
            level=[]
            for _ in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node)
            if order%2==0:
                i=0
                j=len(level)-1
                while i<j:
                    level[i].val,level[j].val=level[j].val,level[i].val
                    i+=1
                    j-=1
            order+=1
        return root