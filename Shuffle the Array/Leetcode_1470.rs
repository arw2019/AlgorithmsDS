impl Solution {
    pub fn shuffle(nums: Vec<i32>, n: i32) -> Vec<i32> { 
        let N = n as usize; 
        let mut res = Vec::with_capacity(2*N);
        let mut val: i32;
        for i in 0..2*N{
            val = if i%2==0 {nums[i/2]} else {x nums[N+i/2]}; 
            res.push(val);
        }
        return res;
    }
}


impl Solution {
    pub fn shuffle(nums: Vec<i32>, n: i32) -> Vec<i32> { 
        let N = n as usize; 
        let mut res = Vec::with_capacity(2*N);
        for i in 0..2*N{
            if (i%2==0){
                res.push(nums[i/2]);
            } else {
                res.push(nums[N+i/2]);
            } 
        }
        return res;
    }
}


impl Solution {
    pub fn shuffle(nums: Vec<i32>, n: i32) -> Vec<i32> { 
        let mut res = Vec::with_capacity(2*n as usize);
        for i in 0..2*n{
            if (i%2==0){
                res.push(nums[(i/2) as usize]);
            } else {
                res.push(nums[(n+i/2) as usize]);
            } 
        }
        return res;
    }
}
