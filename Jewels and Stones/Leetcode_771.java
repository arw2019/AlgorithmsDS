class Solution {
    public int numJewelsInStones(String J, String S) {
        Set<String> jewels = new HashSet<String>();
        for (int i=0; i<J.length(); i++){
            jewels.add(J.substring(i, i+1));
        }
        int res=0;
        for(int i=0; i<S.length(); i++){
            if (jewels.contains(S.substring(i, i+1))) res++;
        }
        return res;
    }
}
