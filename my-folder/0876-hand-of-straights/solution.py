
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n%groupSize != 0:
            return False
        freq={}
        for i in hand:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        
        sorted_freq=sorted(freq.keys())
        for i in sorted_freq:
            if freq[i]>0:
                curr=freq[i]
                for j in range(i,i+groupSize):
                    if freq.get(j,0)<curr:
                        return False
                    freq[j]-=curr
        return True
                    
