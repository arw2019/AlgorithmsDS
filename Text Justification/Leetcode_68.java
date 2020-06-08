class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> res = new ArrayList();
        List<String> cur = new ArrayList();
        int numOfLetters = 0, idx;
        String curRes;
        for (String w: words){
            if ((numOfLetters+w.length() + cur.size()) > maxWidth){
                for (int i=0; i<(maxWidth-numOfLetters); i++){
                    if (cur.size() == 1) idx=0;
                    else idx=i%(cur.size()-1);
                    cur.set(idx, cur.get(idx)+' ');
                }
                curRes="";
                for (String ww: cur) curRes+=ww;
                res.add(curRes);
                cur.clear();
                numOfLetters=0;
            } 
            cur.add(w);
            numOfLetters+=w.length();
        }
        if (cur.size()>0){
            curRes="";
            for (String ww: cur) curRes+=ww+" ";
            curRes = curRes.substring(0, curRes.length()-1); 
            while(curRes.length()<maxWidth) curRes+=" ";
            res.add(curRes);
        }
        return res;
    }
}
