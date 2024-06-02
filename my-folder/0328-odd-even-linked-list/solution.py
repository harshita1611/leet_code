# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        odd=head
        even=head.next
        curr=head.next
        while even and even.next :
            odd.next=odd.next.next
            odd=odd.next

            even.next=even.next.next
            even=even.next

        odd.next=curr

        return head
