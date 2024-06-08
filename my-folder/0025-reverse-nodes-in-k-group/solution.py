# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        prev=None
        curr=head
        next_node=None
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        return prev
    
    def length(self,head):
        count=0
        while head:
            count+=1
            head=head.next
        return count


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k==1:
            return head
        lengthOfLL=self.length(head)

        prev=None
        next_node=None
        count=0
        curr=head

        if k>lengthOfLL:
            return head

        while count<k and curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
            count+=1
        
        head.next=self.reverseKGroup(curr,k)
        return prev
