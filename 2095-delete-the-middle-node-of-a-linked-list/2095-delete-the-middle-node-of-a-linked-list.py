# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        n=len(arr)//2
        new=[]
        for i in range(len(arr)):
            if n==i:
                continue
            else:
                new.append(arr[i])
        dummy=ListNode(0)
        tail=dummy
        for i in new:
            tail.next=ListNode(i)
            tail=tail.next
        return dummy.next
                