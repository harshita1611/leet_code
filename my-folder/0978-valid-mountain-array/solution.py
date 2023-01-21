class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
         if len(arr) >= 3:
            maximum = max(arr)
            index = arr.index(maximum)
            arr_1 = arr[:index]
            arr_2 = arr[index:]

            arr_1_res = False
            arr_2_res = False

            if len(arr_1) == 1 and arr_1[0] < maximum:
                arr_1_res = True
            else:
                for i in range(len(arr_1) - 1):
                    if arr_1[i] < arr_1[i + 1]:
                        arr_1_res = True
                    else:
                        return False

            if len(arr_2) == 1 and arr_2[0] > maximum:
                arr_2_res= True
            else:
                for i in range(len(arr_2) - 1):
                    if arr_2[i] > arr_2[i + 1]:
                        arr_2_res = True
                    else:
                        return False

            return arr_2_res and arr_1_res
