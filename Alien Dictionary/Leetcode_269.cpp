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
        
        set<char> chars, free;
        for (int i=0; i<words.size(); ++i){
            for (int j=0; j<words[i].size(); j++) {
                cout << "i: "<<i<< " j: "<<j << " char: "<<words[i][j] << endl;
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
                cout << "erasing from free: " <<less[i].second << endl; 
            }
            if (free.size()==0) return ""; 
            cout<<"Free: "<< endl;
            for (auto it=free.begin(); it!=free.end(); ++it) { 
                cout<<"*it: "<<*it<<endl;
                order+=*it;
                chars.erase(*it);
            }
            
            cout <<"This is chars: "<<endl;
            for (auto it=chars.begin(); it!=chars.end(); ++it) cout<<"*it: "<<*it<<endl;
            
            tmp.clear(); cout << "New less: " << endl;
            for (auto it=less.begin(); it<less.end(); it++){
                p = *it;
                cout<<p.first<< " " << p.second << endl;
                if (free.count(p.first)==0 && free.count(p.second)==0){
                    cout << "adding to tmp" << endl;
                    tmp.push_back(p);
                }
            }
            less = tmp;
            cout << "tmp size: " << tmp.size() << endl;
            cout << "less size: " << less.size() << endl;
        }
        
        for (auto it=chars.begin(); it!=chars.end(); it++) order += *it;

        return order;
    }
};
