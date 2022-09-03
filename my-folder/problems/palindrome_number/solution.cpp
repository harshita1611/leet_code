class Solution {
public:
    bool isPalindrome(int x) {
    long int n1;
    long int num ;
    num=x;
    if (x<0){
        return false ;
    }
    if(x!=0 && x%10==0){
        return false ;
    }
    long int reverse (0) ;
    while (x!=0) { 
        n1= x%10 ;
        reverse = reverse*10 + n1  ;
        x=x/10; 
    }
    if (num == reverse) {
             return true;
        }
        else {
            return false;
        }
        
        
    }
};