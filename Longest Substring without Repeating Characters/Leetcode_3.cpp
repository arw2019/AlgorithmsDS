class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.length() == 0) return 0;
        int maxLen=1;
        string cur;
        for (char& c: s)
            if (cur.find_first_of(c) == string::npos){
                cur += c;
                if (cur.length() > maxLen) maxLen=cur.length();
            } else {
                size_t pos = cur.find_first_of(c);
                cur = cur.substr(++pos) + c;
            }
        return maxLen;
    }
};
