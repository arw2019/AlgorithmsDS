class Solution {
public:
    int findMin(vector<int>& A) {
        int lo =0, hi = A.size()-1;
        while (hi>0 && A[lo]==A[hi]) hi--;
        int mid;
        while (lo<hi){
            mid = lo + (hi-lo)/2;
            if (A[mid] > A[hi]) lo=mid+1;
            else hi=mid;
        }
        return A[lo];
    }
};
