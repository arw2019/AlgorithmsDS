class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> res(2*n);
        for (int i=0; i<nums.size(); i++){
            res[i] = i%2 ? nums[n+i/2] : nums[i/2];
        } 
        return res;
    }
};
