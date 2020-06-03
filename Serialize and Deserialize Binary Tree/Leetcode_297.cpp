/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
private:
    string vals;

public:
    void write(TreeNode* node){
        if (node == NULL) vals+= " #";
        else{
            vals += " " + to_string(node->val);
            doit(node->left);
            doit(node->right);
        }
    }

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        vals = "";
        write(root);
        cout << vals << endl;
        return vals;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        return NULL;
    }
};
