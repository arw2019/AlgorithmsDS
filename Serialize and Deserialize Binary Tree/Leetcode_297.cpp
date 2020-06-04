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
    string wstr;
    vector <string> rvec; 
    int i;

public:
    void write(TreeNode* node){
        if (node == NULL) wstr+= " #";
        else{
            wstr += " " + to_string(node->val);
            write(node->left);
            write(node->right);
        }
    }

    TreeNode* read(){
        if (rvec[i] == "#") {i++; return NULL;}
        else {
            // cout << "rvec[" << i<<"]: " << rvec[i]<<endl;
            TreeNode* node = new TreeNode(stoi(rvec[i++]));
            node->left = read();
            node->right = read();
            return node;
        }
    }
    
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        wstr = "";
        write(root);
        // cout << wstr << endl;
        return wstr;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        rvec.clear(); i=0;
        istringstream iss(data);
        copy(istream_iterator<string> (iss),
            istream_iterator<string>(),
            back_inserter(rvec));
        return read();
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));
