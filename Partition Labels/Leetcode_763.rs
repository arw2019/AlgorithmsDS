use std::collections::HashMap;

impl Solution {
    pub fn partition_labels(s: String) -> Vec<i32> {
        let n: usize = s.len();
        
        // O(L) space, L=size(alphabet)
        let S: Vec<char> =(&s).chars().collect();
        let mut d: HashMap<char, usize> = HashMap::new();
        for i in 0..n{
            d.insert(S[i], i);
        }
        let mut res: Vec<i32> = Vec::new();
        let mut cur_start: usize = 0;
        let mut cur_end: usize = d[&S[0]];
        
        // O(N) time
        for i in 0..n{
            if d[&S[i]] > cur_end {cur_end = d[&S[i]];}
            if i==cur_end {
                res.push((cur_end-cur_start+1) as i32);
                cur_start = i+1;
            }
        }; 
        return res;
        } 
    }
