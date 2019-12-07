#include <stdlib.h>
#include <limits.h>

class Solution {
public:
    int reverse(int x) {
        int res = 0;
        while (x!=0)
        {
            if (res > 0 and (res > INT_MAX/10 or res * 10 > INT_MAX - x % 10)) /*overflow */
                    return 0;
            if (res < 0 and (res < INT_MIN/10 or res * 10 < INT_MIN - x % 10)) /*underflow */
                    return 0;
            res = res * 10 + x %10; 
            x = x/10;
        }
        return res;
    }
};
