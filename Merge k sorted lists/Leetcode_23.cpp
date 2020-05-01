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
        if (lists.empty()) return NULL;
        
        priority_queue<pair<int, int>> pq;
        for (int i=0; i<lists.size(); ++i){
            if (lists[i] != NULL){
                pq.push(make_pair(-lists[i]->val, i));
            }
        }
        
        ListNode* dummy = new ListNode(INT_MIN);
        ListNode* cur = dummy;
        
        int index;
        while (!pq.empty()){
            index = pq.top().second;
            cur->next = lists[index];
            pq.pop(); 
            lists[index] = lists[index]->next;
            if (lists[index]!= NULL){
                pq.push(make_pair(-lists[index]->val, index));
            } 
            cur = cur->next;
            
        }
        
        return dummy->next;
    }
};
