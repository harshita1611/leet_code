class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        counter=0
        expected = heights.copy()
        expected.sort()
        for i in range(len(heights)):
            if heights[i] != expected[i] :
                counter+=1
        return  counter

obj = Solution()
print(obj.heightChecker([1,1,4,2,1,3]))