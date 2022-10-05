class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int leftsum = 0;
        int rightsum = 0;
        for (int i = 1; i < nums.size(); i++) {
            rightsum += nums[i];
        }
        if (rightsum == 0) {
            return 0;
        }
        for (int i = 1; i < nums.size(); i++) {
            leftsum += nums[i-1];
            rightsum -= nums[i];
            if (leftsum == rightsum) {
                return i;
            }
        }
        if (leftsum == 0) {
            return 0;
        }
        return -1;
    }
};