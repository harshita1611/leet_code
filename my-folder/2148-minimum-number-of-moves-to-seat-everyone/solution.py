class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        n=len(seats)
        i=0
        ans=0
        while i<n:
            ans+= abs(seats[i]-students[i])
            i+=1
        return ans
