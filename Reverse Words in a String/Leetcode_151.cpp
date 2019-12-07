class Solution {
public:
    string reverseWords(string text) {
        istringstream iss(text);
        vector<string> splitText((istream_iterator<string>(iss)),
                                 istream_iterator<string>());
        reverse(splitText.begin(), splitText.end());
        string res;
        for_each(splitText.begin(), splitText.end(), [&](const std::string &piece){ res += piece + ' '; });
        res.pop_back();
        return res;
    }
};
