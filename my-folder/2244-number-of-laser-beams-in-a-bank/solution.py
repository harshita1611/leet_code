class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        arr=[]
        for i in bank:
            arr.append(i.count('1'))
    
        ans=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                print(arr[i]*arr[j])
                if (arr[i]*arr[j]) >0:
                    ans+= arr[i]*arr[j]
                    break
        return ans
