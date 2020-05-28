class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> unique_nums;
        int best = 1, num;
        for (int i=0; i<nums.size(); ++i) unique_nums.insert(nums[i]);
        for (auto it=unique_nums.begin(); it!=unique_nums.end(); it++){
            if (unique_nums.count(*it-1) == 0){
                cout << *it << "  is the start of a sequence" << endl;
                num = *it + 1;
                while(unique_nums.count(num++))
                best = max(best, num - *it);
            }
        }
        return best;
    }
};
