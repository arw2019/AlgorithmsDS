class Solution {
public:
    string removeVowels(string S) {
        string res, vowels="aeiou";
        for (char& c: S){
            if (vowels.find(c) ==string::npos) res+=c;
        }
        return res;
    }
};
