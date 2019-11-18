//find lowest common ancestor with parent pointer. #fb #lca #tree #binarytree O(1) space and O(n) time.

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode *parent;
    TreeNode(int x) : val(x), left(NULL), right(NULL), parent(NULL) {}
};

int getHeight(TreeNode *node) {
    int height = 0;
    while (node) {
        node = node->parent;
        height++;
    }
    return height;
}

TreeNode *lca(TreeNode *node1, TreeNode *node2) {
    if (!node1 || !node2)
        return NULL;

    int height1 = getHeight(node1);
    int height2 = getHeight(node2);

    if (height1 > height2) {
        swap(height1, height2);
        swap(node1, node2);
    }

    while (height1 < height2) {
        if (!node2)
            return NULL;
        node2 = node2->parent;
        height2--;
    }

    while (node1 && node2) {
        if (node1 == node2)
            return node1;
        node1 = node1->parent;
        node2 = node2->parent;
    }

    return NULL;
}