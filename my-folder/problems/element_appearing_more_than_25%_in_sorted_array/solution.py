class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq={}
        n=len(arr)
        for i in arr :
            try:
                freq[i]+=1
            except:
                freq[i]=1
            
            if freq[i]> n//4:
                return i
        
