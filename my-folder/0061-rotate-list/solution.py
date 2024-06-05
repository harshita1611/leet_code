# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head

        size=1
        curr=head #1->2->3->4curr->5
        while curr.next:
            size+=1
            curr=curr.next

        # if size%k==0: 
        #     return head

        k=k%size #2%5==3
        k=size-k #2
        curr.next=head #1->2->3->4->5->1->2->3->4->5
        while k :
            curr=curr.next
            k-=1
        head=curr.next
        curr.next=None
        return head
