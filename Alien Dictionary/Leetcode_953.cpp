class Solution {
private:    
    unordered_map<char, char> aliendict;
public:
    string toAlien(string word){
        string alien = "";
        for (string::iterator it = word.begin(); it < word.end(); it++){
            alien += aliendict[*it];
        }
        return alien; 
    }
    
    bool isGreater(string word1, string word2){
        return toAlien(word2) >= toAlien(word2);
    }
    
    bool isAlienSorted(vector<string>& words, string order) {
        for (int i=0; i<order.size(); ++i){
            aliendict[order[i]] = 'a' + i;
        }
        for (int j=0; j<words.size()-1; j++){
            if (!isGreater(words[j+1], words[j])) return false;
        }
        return true;
    }
};
