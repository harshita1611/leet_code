

int maxSubArray(int* nums, int numsize){
     int maxCurrent = nums[0], maxGlobal = nums[0];
    for(int i = 1;i<numsize;i++){
        maxCurrent = nums[i] > nums[i] + maxCurrent ? nums[i] : nums[i] + maxCurrent;
        if(maxCurrent > maxGlobal){
            maxGlobal = maxCurrent;
        }
    }
    return maxGlobal;
}

