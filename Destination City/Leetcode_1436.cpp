class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        set<string> cities, outgoing;
        for (auto p: paths) {
            cities.insert(p[0]); 
            cities.insert(p[1]);
            outgoing.insert(p[0]);
        }
       
        for (auto city: cities) if (outgoing.count(city) == 0) return city; 
        
        return "";
    }
};
