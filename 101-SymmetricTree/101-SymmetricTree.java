// Last updated: 8/11/2026, 12:25:37 PM
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) return true;

        return result(root.left, root.right);
    }

    public boolean result(TreeNode left, TreeNode right) {
        if (left == null && right == null) return true;

        if (left == null || right == null) return false;

        if (left.val != right.val) return false;

        return result(left.left, right.right) && result(left.right, right.left);
    }
}