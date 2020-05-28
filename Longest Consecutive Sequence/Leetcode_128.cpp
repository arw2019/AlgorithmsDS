class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() == 0) return 0; 
        unordered_set<long int> unique_nums;
        long int num;
        int best = 1;
        for (int i=0; i<nums.size(); ++i) unique_nums.insert(nums[i]);
        for (auto it=unique_nums.begin(); it!=unique_nums.end(); it++){
            if (unique_nums.count(*it-1) == 0){
                num = *it + 1;
                while(unique_nums.count(num++))
                if ((num - *it) > best) best = num - *it;
            }
        }
        return best;
    }
};
