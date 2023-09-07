# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr=head


        def middle(head):
            slow = head
            fast = head
            while slow and fast and fast.next :
                slow=slow.next
                fast=fast.next.next
            return slow

        
        mid= middle(head)

        def reverse(middle):
            curr = middle
            dummy_node = None
            while curr  :
                temp = curr.next
                curr.next = dummy_node
                dummy_node = curr 
                curr = temp 
            return  dummy_node

        second_half = reverse(mid)
        while second_half :
            if curr.val != second_half.val :
                return False
            curr=curr.next
            second_half=second_half.next
        return True
            
