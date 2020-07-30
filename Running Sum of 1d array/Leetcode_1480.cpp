class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> res;
        int tot = 0;
        for (int i: nums) {
            tot += i;
            res.push_back(tot);
        }
        return res;
    }
};
