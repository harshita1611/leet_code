# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 

        ans=0
        while head:
            ans = (ans*10) + (head.val)
            head=head.next
        ans*=2
        if ans==0:
            return ListNode(0)
            
        numbers=[]
        while ans:
            digit=ans%10
            numbers.append(digit)
            ans=ans//10
        
        new_head=ListNode(0)
        curr=new_head
        for i in reversed(numbers):
            curr.next=ListNode(i)
            curr=curr.next
        return new_head.next
