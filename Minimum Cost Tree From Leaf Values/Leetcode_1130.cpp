class Solution {
public:
    int mctFromLeafValues(vector<int>& vals) {
        int ans = 0, N = vals.size();
        vector<int> stack = {INT_MAX};
        for (int v: vals){
            while (stack.back() <= v) {
                int v2 = stack.back();
                stack.pop_back();
                ans += v2 *min(stack.back(), v);
            }
            stack.push_back(v);
        }
        for (int i=2; i < stack.size(); ++i){
            ans += stack[i] * stack[i-1];
        }
        return ans;
    }
};
