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
    int getDecimalValue(ListNode* head) {
        int res = 0;
        ListNode* cur = head;
        while (cur != NULL)
        {
            res = res * 2 + cur->val;
            cur = cur->next;
        }
        return res;
    }
};
