from itertools import combinations

class Solution:
    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:
       
        # O(NlgN) - skip if data guaranteed to be sorted by timestamp
        data = sorted(zip(username, timestamp, website), key=lambda t: t[1])
        
        # O(N)
        user_list = list(set(username))
        user_data = {
            user: [website for uname, _, website in data if uname == user]
            for user in user_list
        }
        
        _3seqs, all_3seqs = {}, set()
        # loop executes O(U) times, U=#users
        for user in user_list:
            # O(M^3) where M=#website visits for user
            # M = O(N) but possibly much less
            _3seqs[user] = {c for c in combinations(user_data[user], 3)}
            all_3seqs |= _3seqs[user]
            
        # O(TlgT) where T=#3-sequences 
        # T=O(N^3) => O(N^3lg(N^3))=O(N^3lgN) worst case
        # but T could be << N^3 for some inputs
        return next(
            iter(
                sorted(
                    all_3seqs,
                    key=lambda _3seq: (
                        -sum(_3seq in user_3seqs for _, user_3seqs in _3seqs.items()),
                        _3seq,
                    ),
                )
            ),
            [],
        )
