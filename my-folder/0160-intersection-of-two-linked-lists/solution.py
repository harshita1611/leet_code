# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None and headB is None :
            return None
        
        s=set()
        while headA:
            s.add(headA)
            headA=headA.next
        
        while headB and headB not in s:
            headB=headB.next
        
        if headB :
            return headB
        else:
            return None
