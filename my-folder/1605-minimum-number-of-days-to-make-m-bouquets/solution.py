class Solution:
    def possible(self,arr,day,m,k):
        count=0
        noOfBoq=0
        n=len(arr)
        for i in range(n):
            if arr[i]<=day:
                count+=1
            else:
                noOfBoq+= (count//k)
                count=0
        noOfBoq+= (count//k)
        if noOfBoq>=m :
            return True
        
        return False
            
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        total_flowers=m*k
        n=len(bloomDay)

        if total_flowers>n:
            return -1

        mini=float('inf')
        maxi=float('-inf')
        for i in range(n):
            mini=min(mini,bloomDay[i])
            maxi=max(maxi,bloomDay[i])

        low=mini
        high=maxi
        while low<=high:
            mid=(low+high)//2
            if self.possible(bloomDay,mid,m,k):
                high=mid-1
            else:
                low=mid+1
        return low
        
