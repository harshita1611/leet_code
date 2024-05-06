# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        dummy_head=ListNode(-1)
        temp_prev=dummy_head
        curr=prev
        while curr:
            if curr.val>=temp_prev.val:
                temp_prev.next=curr
                temp_prev=curr
                curr=curr.next
            else:
                curr=curr.next
        temp_prev.next=None


        new_prev=None
        curr=dummy_head.next
        while curr:
            temp=curr.next
            curr.next=new_prev
            new_prev=curr
            curr=temp
        return new_prev
