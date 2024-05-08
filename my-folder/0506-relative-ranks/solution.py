class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        hashmap={}
        n=len(score)
        for i in range(n):
            hashmap[score[i]]=i

        score.sort(reverse=True)
        
        rank=['']*n
        for i in range(n):
            if i==0:
                rank[hashmap[score[i]]]="Gold Medal"
            elif i==1:
                rank[hashmap[score[i]]]="Silver Medal"
            elif i==2:
                rank[hashmap[score[i]]]="Bronze Medal"
            else:
                rank[hashmap[score[i]]]= str(i+1)
        return rank
