class Solution {
public:
    bool isPathCrossing(string path) {
        vector<pair<int,int>> s;
        int x = 0;
        int y = 0;
        s.push_back({x,y});
        for(char i : path){
            if(i == 'N') y++;
            else if(i == 'S') y--;
            else if(i == 'E') x--;
            else if(i == 'W') x++;
            s.push_back({x,y});
        }
        set<pair<int,int>> se(s.begin(),s.end());
        return s.size() != se.size();
    }
};
