# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        len = 0
        temp = head
        while temp:
            temp = temp.next  
            len += 1
        nodes=len//k
        rem=len%k
        res=[]
        cur=head
        for i in range(k):
            res.append(cur)
            for j in range(nodes-1+(1 if rem else 0)):
                if not cur : break 
                cur=cur.next
            rem -= (1 if rem else 0)
            if cur:
                cur.next , cur = None , cur.next
        return res
