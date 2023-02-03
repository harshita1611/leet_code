class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in digits :
            i=int("".join(str(i)))
            i+=1
        res1 = list(map(int, str(i)))
        return res1

obj = Solution()
print(obj.plusOne([1,2,3]))