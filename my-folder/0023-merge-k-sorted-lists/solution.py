# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans=[]
        for i in range(len(lists)):
            head=lists[i]
            while head :
                ans.append(head.val)
                head=head.next
        
        ans.sort()
        dummy=ListNode(-1)
        temp=dummy
        for i in range(len(ans)):
            temp.next=ListNode(ans[i])
            temp=temp.next
        
        return dummy.next
