class KthLargest(object):
    import heapq 
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)



struct Node {
    Node* left;
    Node* right;
    int val;
    int cnt;
    Node(int v, int c) : left(NULL), right(NULL), val(v), cnt(c) {}
};

class KthLargest {
private:
    Node* insertNode(Node* root, int num) {
        if (!root) {
            return new Node(num, 1);        // return a new node if root is null
        }
        if (root->val < num) {          // insert to the right subtree if val > root->val
            root->right = insertNode(root->right, num);
        } else {                        // insert to the left subtree if val <= root->val
            root->left = insertNode(root->left, num);
        }
        root->cnt++;
        return root;
    }
    int searchKth(Node* root, int k) {
        // m = the size of right subtree
        int m = root->right ? (root->right)->cnt : 0;
        // root is the m+1 largest node in the BST
        if (k == m + 1) {
            return root->val;
        }
        if (k <= m) {
            // find kth largest in the right subtree
            return searchKth(root->right, k);
        } else {
            // find (k-m-1)th largest in the left subtree
            return searchKth(root->left, k - m - 1);
        }
    }
    Node* root;
    int m_k;
public:
    KthLargest(int k, vector<int> nums) {
        root = NULL;
        for (int i = 0; i < nums.size(); ++i) {
            root = insertNode(root, nums[i]);
        }
        m_k = k;
    }
    
    int add(int val) {
        root = insertNode(root, val);
        return searchKth(root, m_k);
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */