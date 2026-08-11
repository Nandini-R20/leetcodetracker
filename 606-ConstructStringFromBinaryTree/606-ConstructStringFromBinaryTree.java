// Last updated: 8/11/2026, 12:22:41 PM
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
public class Solution {
    public String tree2str(TreeNode t) {
        if (t == null) return "";

        String result = "" + t.val;

        if (t.left != null || t.right != null) {
            result += "(" + tree2str(t.left) + ")";
        }

        if (t.right != null) {
            result += "(" + tree2str(t.right) + ")";
        }

        return result;
    }
}