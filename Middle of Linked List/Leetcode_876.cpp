/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        int cnt = 0; // number of nodes in linked lists
        ListNode* cur = head;
        while (cur != NULL)
        {
            ++cnt;
            cur = cur->next;
        }
        int loc;
        loc = cnt/2;
         
        cur = head; 
        int i = 0;
        while (i != loc)
        {
            ++i;
            cur = cur->next;
        }
        return cur;
    }
};
