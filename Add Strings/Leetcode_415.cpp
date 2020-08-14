class Solution {
public:
    string addStrings(string num1, string num2) {
        string res; 
        int carry=0;
        int i=num1.size()-1, j=num2.size()-1;
        int digit1, digit2;
        while(i>=0 || j>=0){
            digit1 = i>=0 ? num1[i--] - '0' : 0;
            digit2 = j>=0 ? num2[j--] - '0' : 0;
            carry += digit1 + digit2;
            res += '0' + carry%10;
            carry /= 10;
        }
        if (carry) res += '0' + carry;
        return string(res.rbegin(), res.rend());
    }
};
