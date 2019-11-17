class Solution {
public:
    int fixedPoint(vector<int>& A) {
        int l=0, r=A.size()-1, m;
        while (l<r)
        {
            m = (l+r)/2;
            if (A[m]<m)
                l = m+1;
            else
                r=m;
        }
        return A[l]==l ? l: -1;
    }
};
