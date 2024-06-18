class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobProfile=[(0,0)]
        for i in range(len(difficulty)):
            jobProfile.append((difficulty[i],profit[i]))
        jobProfile.sort()

        for i in range(len(jobProfile)-1):
            jobProfile[i+1]=( jobProfile[i + 1][0], max(jobProfile[i][1], jobProfile[i + 1][1]))

        netProfit=0
        for i in range(len(worker)):
            ability=worker[i]
            l,r=0,len(jobProfile)-1
            jobProfit=0
            while l<=r:
                mid=(l+r)//2
                if jobProfile[mid][0]<=ability:
                    jobProfit=max(jobProfit,jobProfile[mid][1])
                    l=mid+1
                else:
                    r=mid-1
            netProfit+=jobProfit
        return netProfit
