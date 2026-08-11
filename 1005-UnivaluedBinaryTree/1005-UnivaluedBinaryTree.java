// Last updated: 8/11/2026, 12:21:57 PM
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
    public boolean isUnivalTree(TreeNode root) {
        if(root==null) return true;
        if((root.left!=null && root.val!=root.left.val) || (root.right!=null && root.val!=root.right.val)) return false;
        boolean l = isUnivalTree(root.left);
        boolean r = isUnivalTree(root.right);

        return l && r;
    }
}