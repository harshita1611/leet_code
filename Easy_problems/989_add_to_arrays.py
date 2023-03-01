class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        list_string = list(map(str , num))
        string = ""
        for i in list_string:
            string+=i
        ans = int(string)+k
        ans = str(ans)

        return list(map(int , ans))

obj = Solution()
print(obj.addToArrayForm([1,2,0,0], 34))
