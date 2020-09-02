class Solution {
 private:
  unordered_map<char, char> aliendict;

 public:
  string toAlien(string word) {
    string alien = "";
    for (string::iterator it = word.begin(); it < word.end(); it++) {
      alien += aliendict[*it];
    }
    return alien;
  }

  bool isGreater(string word1, string word2) {
    return toAlien(word2) >= toAlien(word2);
  }

  bool isAlienSorted(vector<string>& words, string order) {
    for (int i = 0; i < order.size(); ++i) {
      aliendict[order[i]] = 'a' + i;
    }
    for (int j = 0; j < words.size() - 1; j++) {
      if (!isGreater(words[j + 1], words[j])) return false;
    }
    return true;
  }
};

// alternative solution
// doesn't use an associative container

class Solution {
 public:
  bool isAlienSorted(vector<string>& words, string order) {
    vector<char> indicies(26);
    for (int i = 0; i < order.size(); i++) {
      indicies[order[i] % 26] = i;
    }

    for (int i = 0; i < words.size() - 1; i++) {
      string& word1 = words[i];
      string& word2 = words[i + 1];
      int len1 = word1.size();
      int len2 = word2.size();
      bool same = true;
      for (int j = 0; j < min(len1, len2); j++) {
        if (indicies[word1[j] % 26] > indicies[word2[j] % 26]) {
          return false;
        } else if (indicies[word1[j] % 26] < indicies[word2[j] % 26]) {
          same = false;
          break;
        }
        if (same && len1 > len2) return false;
      }
    }
    return true;
  }
};
