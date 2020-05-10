class Solution {
public:
    string alienOrder(vector<string>& words) {
        vector <pair<char, char>> less, tmp;
        pair<char, char> p;
        for (int i=0; i<words.size()-1; ++i){
            string word1=words[i], word2=words[i+1];
            for (int j=0; j<min(word1.size(), word2.size()); ++j){
                char char1=word1[j], char2=word2[j];
                if (char1 != char2){
                    p = make_pair(char1, char2); 
                    less.push_back(p);
                    break;
                }
            }
        }
        
        
        set<char> chars, free;
        for (int i=0; i<words.size(); ++i){
            for (int j=0; j<words[i].size(); j++) {
                chars.insert(words[i][j]);
            }
        }

       
        string order="";
        if (less.size() == 0){
            for (int i=0; i<words.size()-1; ++i) {
                if (words[i+1].size() < words[i].size()) return "";
            }
        }
       
        while (less.size() > 0){
            free = chars;
            for (int i=0; i<less.size(); ++i){
                free.erase(less[i].second); 
            }
            if (free.size()==0) return ""; 
            for (auto it=free.begin(); it!=free.end(); ++it) { 
                order+=*it;
                chars.erase(*it);
            }
            
            tmp.clear(); 
            for (auto it=less.begin(); it<less.end(); it++){
                p = *it;
                if (free.count(p.first)==0 && free.count(p.second)==0) tmp.push_back(p);
            }
            less = tmp;
        }
        
        for (auto it=chars.begin(); it!=chars.end(); it++) order += *it;

        return order;
    }
};
