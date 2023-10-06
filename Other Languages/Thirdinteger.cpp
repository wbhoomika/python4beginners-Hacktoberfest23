#third integer
class Solution {
public:
    int integerBreak(int n) {
        if(n<=3){
            return n-1;
        }
        if(n==4){
            return 4;
        }
        if(n==5){
            return 6;
        }
        if(n==6){
            return 9;
        }
        int ans = 1;
        while(n!=0){
            if(n==4||n==2){
                ans = ans*n;
                break;
            }
            ans = ans*3;
            n = n-3;
        }
        return ans;
    }
};
