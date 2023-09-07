# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next :
            return None
        slow = head
        fast = head
        curr=head
        while slow and fast and fast.next :
            slow = slow.next
            fast = fast.next.next

        while curr.next != slow:
            curr=curr.next
        curr.next=slow.next
        return head
