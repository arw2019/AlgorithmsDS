class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> d;
        for (int i = 0; i < nums.size(); ++i)
        {
            if (d.find(target - nums[i]) != d.end())
            {
                return {d[target - nums[i]], i};
            }
        d[nums[i]] = i;    
        }
        return {};
    }
};
