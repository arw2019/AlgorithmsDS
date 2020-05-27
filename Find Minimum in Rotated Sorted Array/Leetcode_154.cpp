// binary search solution

class Solution {
public:
    int findMin(vector<int>& nums) {
        int lo=0, hi=nums.size()-1, mid;
        // This step is O(N) for worst case input.
        while ((hi>0) & (nums[lo]==nums[hi])) hi--;
        while (lo<hi){
            mid = lo +(hi-lo)/2;
            if (nums[mid] > nums[hi]) lo=mid+1;
            else hi=mid;
        }
        return nums[lo];
    }
};
