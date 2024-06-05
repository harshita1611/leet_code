# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        curr=head
        arr=[]
        while curr:
            arr.append(curr.val)
            curr=curr.next
        
        arr.sort()

        curr=head
        for i in arr:
            curr.val=i
            curr=curr.next
        
        return head
