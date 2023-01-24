class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counter=0
        expected = heights.copy()
        expected.sort()
        for i in range(len(heights)):
            if heights[i] != expected[i] :
                counter+=1
        return  counter
