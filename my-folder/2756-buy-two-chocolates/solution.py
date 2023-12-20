class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        m1=m2=101
        for i in prices:
            if i< m1:
                m2=m1
                m1=i
            elif i<m2:
                m2=i
        return money if (m1+m2)> money else money-(m1+m2)
