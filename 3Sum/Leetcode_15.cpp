class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        map<int, int> table;
        for (int i=0; i<nums.size(); ++i) {
            if (table.count(nums[i]) > 0) {table[nums[i]]++;} 
            else {table[nums[i]] = 1;}
            // cout << "number: " << nums[i] << " count: " << table[nums[i]] << endl;
        }
        vector<int> uniqueNums;
        uniqueNums.reserve(table.size());
        for (auto const& imap: table)
            uniqueNums.push_back(imap.first);
        
        set<vector<int>> res;
       
        int n1, n2, n3; vector<int> cur, tmp;
        for (int i=0; i<uniqueNums.size(); ++i){
            n1 = uniqueNums[i];
            for (int j = i+1; j<uniqueNums.size(); ++j){
                n2 = uniqueNums[j]; 
                n3 = -n1-n2;
                // cout << "n1: " << n1 << ", n2: " << n2 << ", n3: " << n3 << endl;
                cur ={ n1, n2, n3};
                sort(cur.begin(), cur.end());
                if ((n3 == n1) || (n3 == n2)){
                    if (table[n3] >= 2)
                        res.insert(cur);
                } else if (table.count(n3) > 0) {res.insert(cur);}
            }
        }
        
        if (table[0] >= 3) {
            res.insert({0,0,0});}
        
        vector<vector<int>> ans;
        ans.assign(res.begin(), res.end());
        
        return ans;
    }
};
