class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        flag = False
        for i in range(len(arr)):
            for j in range(i, len(arr), 1):
                if (arr[j] * 2 == arr[i] or arr[i] * 2 == arr[j]) and i!=j:
                    flag = True

        return flag