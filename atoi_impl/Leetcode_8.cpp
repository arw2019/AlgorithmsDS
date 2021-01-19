class Solution {
public:
  int myAtoi(string s) {
    bool started = false, isNegative = false;
    int res = 0;
    for (const char &c : s) {
      if (!started && (c == '+' || c == '-')) {
        started = true;
        isNegative = c == '-';
      } else if (c >= '0' && c <= '9') {
        started = true;
        if (isNegative) {
          if (INT_MIN / 10 > res) {
            return INT_MIN;
          }
          res *= 10;
          if (INT_MIN + (c - '0') >= res)
            return INT_MIN;
          res -= (c - '0');
        } else {
          if (INT_MAX / 10 < res) {
            return INT_MAX;
          }
          res *= 10;
          if (INT_MAX - (c - '0') <= res)
            return INT_MAX;
          res += (c - '0');
        }
      } else if ((started && isspace(c)) || (!isspace(c))) {
        break;
      }
    }
    return res;
  }
};
