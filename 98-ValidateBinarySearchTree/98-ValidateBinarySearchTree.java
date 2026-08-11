// Last updated: 8/11/2026, 12:25:46 PM
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
    TreeNode prev = null;

    public boolean isValidBST(TreeNode root) {
        if (root == null) 
            return true;
if (!isValidBST(root.left))
            return false;
 if (prev != null && root.val <= prev.val)
            return false;
System.out.print(root.val + " ");
        prev = root;

        return isValidBST(root.right);
    }
}