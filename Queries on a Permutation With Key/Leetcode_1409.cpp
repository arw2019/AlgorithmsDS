/*
Time complexity: O(m*n) where n=len(queries)
since all list operations are linear time
*/

class Solution {
public:
    vector<int> processQueries(vector<int>& queries, int m) {
        vector<int> res(queries.size());
        
        list<int> P;
        for (int i=1; i<=m; ++i) P.emplace_back(i);
           
        int idx;
        for (int j=0; j<queries.size(); ++j){
            // cout<<"query: "<<queries[j]<<endl;
            list<int>::iterator it; idx=0;
            for (it=P.begin(); it!=P.end(); it++){
                // cout<<"*it="<<*it<<endl;
                if (*it==queries[j]) {
                    // cout<<"FOUND"<<idx<<endl;
                    res[j] = idx;
                    break;
                }
                idx++;
            }
            P.erase(it);
            P.emplace_front(queries[j]);
        }
        return res;
    }
};
