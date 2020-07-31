// string manipulations + STL sort
class Solution {
public:
    bool compareLetterLogs(string log1, string log2){
        size_t pos1 = log1.find(' '), pos2 = log2.find(' ');
        string log1_id_at_back = log1.substr(pos1+1) + ' ' + log1.substr(0, pos1);
        string log2_id_at_back = log2.substr(pos2+1) + ' ' + log2.substr(0, pos2);
        return (log1_id_at_back < log2_id_at_back);
    }
    
    vector<string> reorderLogFiles(vector<string>& logs) {
        vector<string> letter_logs, digit_logs, res;
        for(string& log: logs){
            size_t pos = log.find(' ');
            if (isdigit(log[++pos])) digit_logs.push_back(log);
            else letter_logs.push_back(log);
        }
        
        sort(letter_logs.begin(), letter_logs.end(), [this](string log1, string log2){
             return (compareLetterLogs(log1,log2));});
        
        res.insert(res.end(), letter_logs.begin(), letter_logs.end());
        res.insert(res.end(), digit_logs.begin(), digit_logs.end());
       
        return res;
    }
};
