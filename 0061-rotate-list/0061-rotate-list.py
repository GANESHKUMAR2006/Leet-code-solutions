# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l1=[]
        while head:
            l1.append(head.val)
            head=head.next
        if l1:
            k=k%len(l1)
        l1[:]=l1[-k:]+l1[:-k]
        dummy=ListNode(0)
        tail=dummy
        for i in l1:
            tail.next=ListNode(i)
            tail=tail.next
        return dummy.next