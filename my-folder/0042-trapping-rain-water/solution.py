class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        sum_trap=0
        left_ptr=0
        right_ptr=n-1

        left_max=0
        right_max=0

        while left_ptr <= right_ptr :
            if height[left_ptr]<= height[right_ptr] :
                if height[left_ptr]>left_max:
                    left_max=height[left_ptr]
                else :
                    sum_trap+= left_max-height[left_ptr]
                
                left_ptr+=1
                
            else:
                if height[right_ptr]>right_max:
                    right_max=height[right_ptr]
                else:
                    sum_trap+= right_max-height[right_ptr]

                right_ptr-=1
            
        return sum_trap
