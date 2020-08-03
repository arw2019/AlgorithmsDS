impl Solution {
    pub fn num_jewels_in_stones(j: String, s: String) -> i32 {
        let mut ans = 0;
        for c in s.chars(){
            if j.contains(c) { ans += 1; } 
        }
        return ans;
    }
}
