/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
// woefully slow 
class Solution {
private:
  int dfs(TreeNode* node) {
        return !node ? 0: max(dfs(node->left), dfs(node->right)) + 1;
    };    
public:
    int diameterOfBinaryTree(TreeNode* root) {
        return !root ? 0 : max(dfs(root->left) + dfs(root->right), 
                max(diameterOfBinaryTree(root->left),  diameterOfBinaryTree(root->right)));
    }

};
