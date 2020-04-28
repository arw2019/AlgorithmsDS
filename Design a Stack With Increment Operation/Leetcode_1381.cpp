// first version 

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



// another version

class CustomStack {
    private:
    int *stack;
    int head;
    int tail;
    int elem;
    int mx;
public:
    CustomStack(int maxSize) {
        stack = (int *) malloc(maxSize*sizeof(int));
        head = 0;
        tail = 0;
        elem = 0;
        mx = maxSize;
    }
    
    void push(int x) {
        if (elem < mx){
            stack[head] = x;
            elem++; 
            head++;
        }
    }
    
    int pop() {
        if (elem==0){
            return -1;
        }
        else{
            head--;
            elem--;
            return stack[head];
        }
    }
    
    void increment(int k, int val) {
        if (k>elem){
            for (int i=elem-1; i>=0; i--){
                stack[i] += val;
            }
        } 
        else {
            for (int i=k-1; i>=0; i--){
                stack[i] += val;
            }
        }
    }
};

static const int _ = [](){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return 0;
}();

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */
