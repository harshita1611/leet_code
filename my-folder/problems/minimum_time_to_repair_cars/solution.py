class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def canBeRepaired(ranks,cars,timetaken):
            carsFixed=0
            n=len(ranks)
            for i in range(n):
                carsFixed += int(math.sqrt(timetaken/ranks[i]))
            return carsFixed>=cars
        
        def binary_search(ranks,cars):
            low=0
            high=(max(ranks))*cars*cars
            ans=high
            while low<=high:
                mid=(low+high)//2
                if canBeRepaired(ranks,cars,mid):
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans
        
        return binary_search(ranks,cars)