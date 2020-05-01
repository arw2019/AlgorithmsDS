/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) return nullptr;
        priority_queue<pair<int, int>> pq;
        for (int i=0; i<lists.size(); ++i){
            if (lists[i] != NULL){
                pq.push(make_pair(lists[i]->val, i));
            }
        }
        ListNode* res(0);
        return res;
    }
};
