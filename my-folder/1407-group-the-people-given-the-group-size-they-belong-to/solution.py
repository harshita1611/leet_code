class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        freq={}
        for i in groupSizes:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        
        ans=[]
        for i in freq:
            temp=[]
            for j in range(len(groupSizes)):
                if groupSizes[j]==i:
                    temp.append(j)
                if len(temp)==i:
                    ans.append(temp)
                    temp=[]
                
        return ans  
