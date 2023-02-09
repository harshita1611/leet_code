class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        count = 0
        arr=[]
        for i in fruits:
            arr.append(fruits.count(i))

        return arr
obj  =Solution()
print(obj.totalFruit([1,2,1]))