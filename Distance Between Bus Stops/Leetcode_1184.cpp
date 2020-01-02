class Solution {
public:
    int distanceBetweenBusStops(vector<int>& distance, int start, int destination) {
        
        if (start > destination) {
            int dummy = start;
            start = destination;
            destination = dummy;
        }
        
        int ck = 0;
        for (int i=start; i < destination; ++i) ck += distance[i];
        int cck = accumulate(distance.begin(), distance.end(), 0) - ck;
        
        return min(ck, cck);
    }
};
