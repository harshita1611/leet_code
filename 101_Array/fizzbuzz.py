class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result = ""
        result_list = []
        flag = 0
        for i in range(1,n+1) :
            if i%3==0 :
                result+= "Fizz"
                flag=1
            if i%5==0 :
               result+="Buzz"
               flag=1
            if flag==0 :
                result+= str(i)
        result_list.append(result)
        print(result_list)
obj = Solution()
obj.fizzBuzz(15)