/*
k = lists.size(); N = total number of nodes in all input lists;
Time complexity:
 - To build priority queue: O(k)
 - To create result: O(N*lgk)
Space complexity: O(k) to store the heap
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

// same idea, another implementation. Slightly cleaner IMO

class Solution {
public:
    struct CompareListNode{
      bool operator()(ListNode* node1, ListNode* node2) {return node1->val > node2->val;}  
    };
    
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, CompareListNode> pq;
        
        for (ListNode* node: lists) {if (node != NULL) {pq.push(node);}}
        
        ListNode* dummy_head = new ListNode(INT_MIN);
        ListNode *cur = dummy_head;
        
        while(!pq.empty()){
            cur->next = pq.top();
            pq.pop();
            if (cur->next->next != NULL) {pq.push(cur->next->next); }
            cur = cur->next;
        }
        return dummy_head->next;
    }
};

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
