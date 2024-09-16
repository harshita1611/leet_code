class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurance={char:idx for idx,char in enumerate(s)}
        partitions=[]
        start=0
        end=0
        for i, char in enumerate(s):
            end=max(end,last_occurance[char])
            if i==end:
                partitions.append(i-start+1)
                start=i+1
        return partitions
                
