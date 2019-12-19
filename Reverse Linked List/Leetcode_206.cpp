/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

// iterative

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        
        ListNode* cur = head; ListNode* prev = NULL; ListNode* next = NULL; 
        
        while (cur != NULL)
        {
            next = cur->next;
            cur->next = prev;
            prev = cur;
            cur = next;
        }
        
        return prev;
    }
};

// recursive
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        
        if (!head || !(head->next))
        {
            return head;
        }
        
        ListNode* tmp = reverseList(head->next);
        head -> next -> next = head;
        head -> next = NULL;
        return tmp;
    }
};
