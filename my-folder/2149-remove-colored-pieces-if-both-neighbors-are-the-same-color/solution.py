class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        Alice_move , bob_move=0,0
        for i in range(1,len(colors)-1) :
            if colors[i]==colors[i+1]==colors[i-1] :
                if colors[i]=='A':
                    Alice_move+=1
                elif colors[i]=='B':
                    bob_move+=1
        if Alice_move > bob_move :
            return True
        return False
