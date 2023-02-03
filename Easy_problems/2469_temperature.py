# class Solution:
#     def convertTemperature(self, celsius: float) -> list[float]:
#         return [celsius+273.15, celsius*1.80+32.0]
#
# obj =Solution()
# print(obj.convertTemperature(36.50)
# )len(num_list)//2])
# llst=reversed(list(range(1,11)))
# print(llst)
for i in range(int(input())):
    n = int(input())
    s = input()
    count=0
    for i in s :
        if i=="1":
            count+=1
    print(min(count, n-count+1))
