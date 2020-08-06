class Solution {
    public int dietPlanPerformance(int[] calories, int k, int lower, int upper) {
        int T=0, points=0;
        for (int i=0; i<calories.length+1; i++){
            if (i<k) T+=calories[i];
            else{
                if (T<lower) points--;
                if (T>upper) points++;
                if (i < calories.length) T += (calories[i] - calories[i-k]);
                else break;
            }
        }
        return points;

    }
}
