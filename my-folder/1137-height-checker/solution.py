class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=0
        n=len(heights)
        expected=sorted(heights)
        for i in range(n):
            if heights[i]!= expected[i]:
                count+=1
        return count
