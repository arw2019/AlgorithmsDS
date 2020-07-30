/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// O(N) time, O(h) space
// a-la postorder traversal
// slower on LC than recursive (presumably b/c overhead)

class Solution {
private:
    typedef struct Status {
        Status(): numTargets(0), ancestor(NULL) {}
        int numTargets;
        TreeNode* ancestor;
    } Status;
    
    Status* lca_helper(TreeNode* root, TreeNode* p, TreeNode* q){
        Status* curStatus = new Status;
        if (root == NULL) return curStatus; 
            
        Status* left = lca_helper(root->left, p, q);
        if (left->numTargets == 2) return left;
        else curStatus->numTargets += left->numTargets;
        
        Status* right = lca_helper(root->right, p, q);
        if (right->numTargets == 2) return right;
        else curStatus->numTargets += right->numTargets;
     
        if ((p->val == root->val) || (q->val == root->val)) curStatus->numTargets += 1;
        if (curStatus->numTargets == 2) curStatus->ancestor = root;
        return curStatus;
    };

public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        return lca_helper(root, p, q)->ancestor;
    }
};

// O(N^2) time, O(h) space
// recursion
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if ((root == NULL) || (root==p) || (root==q)) return root;
        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);
        if ((left != NULL) && (right != NULL)){
            return root;
        } else if (left != NULL) return left;
        else return right;
    }
};

