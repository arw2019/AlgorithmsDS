class Solution {
public:
    string alienOrder(vector<string>& words) {
        vector <string> less;
        for (int i=0; i<words.size()-1; ++i){
            string word1=words[i], word2=words[i+1];
            for (int j=0; j<min(word1.size(), word2.size()); ++j){
                char char1=word1[j], char2=word2[j];
                if (char1 != char2){
                    string pair = string() + char1+char2; cout<<"pair: " <<pair<<endl;
                    less.push_back(pair);
                    break;
                }
            }
        }
        
        set<char> chars;
        for (int i=0; i<words.size(); i++){
            for (int j=0; j<words.size(); ++j) chars.insert(words[i][j]);
        }
       
        
        return "";
    }
};
