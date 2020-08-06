impl Solution {
    pub fn diet_plan_performance(calories: Vec<i32>, k: i32, lower: i32, upper: i32) -> i32 {
        let mut T: i32 = 0; 
        let mut points: i32 = 0;
        let k: usize = k as usize;
        let n=calories.len();
        for (i, c) in calories.iter().enumerate(){
            if (i<k){T = T + c;}
            else {
                if (T > upper) {points = points + 1};
                if (T< lower) {points = points - 1};
                T = T - calories[i-k] + c;
            }
        } 
        if (T > upper) {points = points + 1};
        if (T< lower) {points = points - 1};
        return points;
    }
}
