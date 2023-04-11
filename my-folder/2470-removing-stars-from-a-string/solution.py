class Solution:
    def removeStars(self, s: str) -> str:
        str1=list(s)
        # print(str1)
        list1=[]
        for i in range(len(str1)):
            # print(str1[i])
            if str1[i]!="*":
                list1.append(str1[i])
            # print(list1)
            if str1[i]=="*":
                list1.pop()
                # last=
                # str1.pop(i)
        res=""
        res=res.join(list1)
        return res
