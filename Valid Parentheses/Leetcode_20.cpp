class Solution {
public:
    bool isValid(string s) {
        stack<char> parens;
        for (const auto& c: s) {
            switch(c) {
                case '(': parens.push(')'); break;
                case '[': parens.push(']'); break;
                case '{': parens.push('}'); break;
                default:
                    if (parens.empty() || c != parens.top()) return false;
                    else parens.pop();
            }
        }
        return parens.empty();
    }
};
