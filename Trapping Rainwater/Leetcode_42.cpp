class Solution {
public:
    int trap(vector<int>& height) {
        int ans = 0;
        int l = 0, r = height.size() - 1;
        int lMax = 0, rMax = 0;
        while (l<r){
            lMax = max(lMax, height[l]);
            rMax = max(rMax, height[r]);
            if (lMax < rMax) ans += max(0, lMax - height[l++]);
            else ans += max(0, rMax - height[r--]);
        }
        return ans;
    }
};
