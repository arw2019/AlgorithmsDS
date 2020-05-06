class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.size()==0) return false;
        int lo=0, hi=nums.size()-1;
        while (hi>0 && nums[hi]==nums[0]) hi--;
        int mid;
        bool b_target=nums[0]>target, b_mid;
        while (lo<=hi){
            mid = lo + (hi-lo)/2;
            b_mid = nums[0] > nums[mid]; 
            if (nums[mid] == target) return true;
            if (b_mid<b_target || (b_mid == b_target && nums[mid]< target)) {
                lo = mid+1;
            } else hi = mid-1;
        }
        return false;
    }
};
