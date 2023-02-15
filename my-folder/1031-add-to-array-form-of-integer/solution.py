class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        list_string = list(map(str , num))
        string = ""
        for i in list_string:
            string+=i
        ans = int(string)+k
        ans = str(ans)

        return list(map(int , ans))
