class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total = 0
        for i in range(0, len(customers)):
            if i < minutes:
                total += customers[i]
            elif grumpy[i] == 0:
                total += customers[i]
        maxCustomer = total
        l,r=0,minutes

        while r<len(customers):
            if grumpy[r]==1:
                total+=customers[r]
            if grumpy[l]==1:
                total-=customers[l]
            
            l+=1
            r+=1

            maxCustomer = max(maxCustomer,total)
        
        return maxCustomer
