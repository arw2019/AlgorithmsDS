class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int tot = 0;
        for (auto n: nums){
            tot ^= n;
        }
        return tot;
    }
};
