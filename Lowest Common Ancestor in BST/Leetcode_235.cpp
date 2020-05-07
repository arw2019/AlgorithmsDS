/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (p->val > q->val) {
            TreeNode* tmp = p;
            p = q;
            q = tmp;
        }
        if (root->val < p->val) return lowestCommonAncestor(root->right, p, q);
        else if (root->val > q->val) return lowestCommonAncestor(root->left, p, q);
        else return root;
    }
};

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (p->val > q->val) {
            TreeNode* tmp = p;
            p = q;
            q = tmp;
        }
        while (root->val < p->val || root->val > q->val){
            while(root->val < p->val) root=root->right;
            while(root->val > q->val) root=root->left;
        }
        return root;
    }
};
