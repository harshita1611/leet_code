class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = []
        # ans[0]=not lost any match
        # ans[1]=lost exactly one match

        freq = {}
        for i in matches:
            if i[1] in freq:
                freq[i[1]] += 1
            else:
                freq[i[1]] = 1

        x = set()
        y = set()
        for i in matches:
            if i[0] not in freq:
                x.add(i[0])

        for i in freq:
            if freq[i] == 1:
                y.add(i)


        ans.append(sorted(list(x)))
        ans.append(sorted(list(y)))
        
        return ans