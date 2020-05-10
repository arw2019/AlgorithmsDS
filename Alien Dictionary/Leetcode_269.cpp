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
                    p= make_pair(char1, char2); 
                    cout<<"pair: " << p.first << " " << p.second<<endl;
                    less.push_back(p);
                    break;
                }
            }
        }
        
        for (auto p: less) cout<<p.first<<" "<<p.second<<endl;
        
        set<char> chars;
        for (int i=0; i<words.size(); ++i){
            for (int j=0; j<words.size()-1; ++j) {
                cout << "i: "<<i<< " j: "<<j << " char: "<<words[i][j] << endl;
                chars.insert(words[i][j]);
            }
        }

       
        for (auto it=chars.begin(); it!=chars.end(); ++it) cout<<"*it: "<<*it<<endl;
        
        
        string order="";
        if (less.size() == 0){
            for (int i=0; i<words.size()-1; ++i) {
                if (words[i+1].size() < words[i].size()) return "";
            }
        }
       
        while (less.size() > 0){
            set<char> free = chars;
            for (int i=0; i<less.size(); ++i){
                free.erase(less[i].second); 
            }
            for (auto it=free.begin(); it!=free.end(); ++it) cout<<"*it: "<<*it<<endl;
            for (auto it=free.begin(); it!=free.end(); ++it) {
                order+=*it;
                chars.erase(*it);
            }
            tmp.clear();
            for (auto it=less.begin(); it<less.end(); it++){
                pair<char, char> p = *it;
                if (!chars.count(p.first) && !chars.count(p.second)) tmp.push_back(p);
            }
            less = tmp;
        }
        
        for (auto it=chars.begin(); it!=chars.end(); it++) order += *it;

        return order;
    }
};
