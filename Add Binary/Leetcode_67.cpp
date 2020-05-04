class Solution {
public:
    string addBinary(string s1, string s2) {
        reverse_iterator<string::iterator> it1 = s1.rbegin();
        reverse_iterator<string::iterator> it2 = s2.rbegin();
        
        bool finished = false; int carry=0, cur=0;
        string res = "";
        
        while (!finished){
            //cout<<*it1<<' '<<*it2<<' '<<res<<endl;
            cur = carry;
            if ((it1!=s1.rend()) && (*(it1++)) == '1') {cur++;}
            if ((it2!=s2.rend()) && (*(it2++)) == '1') {cur++;}
            
            if (cur%2) {
                res += '1';
            }
            else {
                res += '0';
            }
            carry=cur/2; 
            finished = (it1==s1.rend()) &&  (it2==s2.rend()) && (carry==0);
        }
        
        reverse(res.begin(), res.end());
        
        return res;
    }
};
