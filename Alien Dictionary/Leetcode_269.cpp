class Solution {
public:
    string alienOrder(vector<string>& words) {
        vector <pair<char, char>> less;
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

        return "";
    }
};
