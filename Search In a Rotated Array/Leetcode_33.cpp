class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.size()==0) return -1;
        int lo=0, hi=nums.size()-1, mid;
        while (lo<=hi){
            mid = lo + (hi-lo)/2;
            cout<<mid<<" "<<nums[mid]<<endl;
            if (nums[mid] == target) return mid;
            if (((nums[0]<nums[mid]) && (nums[0]>target)) || (nums[mid] < target)) {
                lo = mid+1;
            } else hi = mid-1;
        }
        return -1;
    }
};
