/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// O(N) time, O(h) extra space

class Solution {
public:
    
    vector<int> postorderTraversal(TreeNode* root) {
        if (root == NULL) {
            return vector<int> {};
        }
        if (root->left == NULL and root ->right == NULL){
            return vector<int> {root->val};
        }
        vector<int> ans;
        vector<int> ansLeft = postorderTraversal(root->left);
        ans.insert(ans.end(), ansLeft.begin(), ansLeft.end());
        vector<int> ansRight = postorderTraversal(root->right);
        ans.insert(ans.end(), ansRight.begin(), ansRight.end());
        ans.push_back(root->val);
        
        return ans;
        
    }
};
