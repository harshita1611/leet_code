class Solution {
public:

    int mySqrt(int x) {
        int start=0;
        int end=x;
        long long ans=0,sqaure=0,mid;
        if(x==0) return 0;
        while(start<=end){
            mid=(start+end)/2;
            sqaure=(mid * mid );
            if(sqaure<=x){
                ans=mid;
                start=mid+1;
            }else if(x>sqaure){
                start=mid+1;
            }else{
                end=mid-1;
            }
        }
        return ans;

    }
};
