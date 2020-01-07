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
    int dis;
    int max(int a, int b){
        return a>b?a:b;
    }
    int diameterOfBinaryTree(TreeNode* root) {
        dis = 0;
        dfs(root);
        return dis;
    }
    int dfs(TreeNode* root){
        if (root==NULL) return 0;
        int left = dfs(root->left);
        int right = dfs(root->right);
        dis = max(dis, left+right);
        return 1 + max(left, right);
    }

};
