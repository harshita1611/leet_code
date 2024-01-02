class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = {}
        ans = []

        for i in nums :
            if i in freq:
                freq[i] +=1
            else:
                freq[i] = 1

        while max(freq.values()) > 0:
            curr = []
            for key, value in freq.items():
                if value :
                    curr.append(key)
                    freq[key]-=1

            ans.append(curr)
            
        return ans