# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        arr.reverse()
        arr=arr[:n-1]+arr[n:]
        arr.reverse()
        dummy=ListNode(0)
        tail=dummy
        for i in arr:
            tail.next=ListNode(i)
            tail=tail.next
        return dummy.next