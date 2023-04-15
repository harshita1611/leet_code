# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode(0)
        current=head
        carry=0
        while l1!=None or l2!=None or carry!=0:
            if l1:
                x=l1.val
            else:
                x=0
            if l2:
                y=l2.val
            else:
                y=0
            columnSum = x+y + carry
            carry=columnSum//10
            newNode=ListNode(columnSum%10)
            current.next=newNode
            current=newNode
            if l1 :
                l1=l1.next
            else :
                None
            if l2 :
                l2=l2.next
            else :
                None
        return head.next
