class Solution {
private:    
    unordered_map<char, char> aliendict;
public:
    bool greaterThan(string word, string order){
       return true; 
    }
    
    bool isAlienSorted(vector<string>& words, string order) {
        for (int i=0; i<order.size(); ++i){
            aliendict['a'+i] = order[i];
            cout << 'a'+i << " " << aliendict['a'+i] << endl;
        }
        return false;
    }
};
