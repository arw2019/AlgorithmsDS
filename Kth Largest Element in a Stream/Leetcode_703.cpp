class KthLargest {
private:
    int K;
    priority_queue<int> pq;
    
public:
    KthLargest(int k, vector<int>& nums) {
        K = k;
        for (auto it=nums.begin(); it!=nums.end(); ++it){
            pq.push(-*it);
            if (pq.size() > K) pq.pop();
        }
    }
    
    int add(int val) {
        pq.push(-val);
        if (pq.size()>K) pq.pop();
        return -pq.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
