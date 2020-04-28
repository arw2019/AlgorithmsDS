class CustomStack {

private:
    int capacity;
    vector<int> stack;
    int n = 0;
    
public:
    CustomStack(int maxSize) {
        capacity = maxSize;
        vector<int> arr(capacity, 0);
        stack = arr;
    }
    
    void push(int x) {
        if (n < capacity){
            stack[n] = x;
            n++;
        }
    }
    
    int pop() {
        int value;
        if (n>0){
            value = stack[n-1];
            n--;}
        else {
            value=-1;
        }
        return value;
    }
    
    void increment(int k, int val) {
        for (int i=0; i<k and i<n; ++i){
            stack[i] += val;
        }
    }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */
