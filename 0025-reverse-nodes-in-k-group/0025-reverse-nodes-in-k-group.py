# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        while True:
            kth=prev
            for _ in range(k):
                kth=kth.next
                if kth is None:
                    return dummy.next
            group=kth.next
            p=group
            curr=prev.next
            while curr!=group:
                temp=curr.next
                curr.next=p
                p=curr
                curr=temp
            temp=prev.next
            prev.next=kth
            prev=temp