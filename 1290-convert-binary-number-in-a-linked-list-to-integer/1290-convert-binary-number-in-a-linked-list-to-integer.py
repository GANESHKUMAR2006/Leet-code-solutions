# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        cur=head
        count=0
        while cur is not None:
            count=count*2
            count+=cur.val
            cur=cur.next
        return count