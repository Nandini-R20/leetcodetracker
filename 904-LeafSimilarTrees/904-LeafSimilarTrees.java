// Last updated: 8/11/2026, 12:22:11 PM
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
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
    List<Integer> l1 = new ArrayList<>();
    List<Integer> l2 = new ArrayList<>();

    InOrder(root1, l1);
    InOrder(root2, l2);

    return l1.equals(l2);
}

private void InOrder(TreeNode node, List<Integer> leaves) {
    if (node == null) return;
    if (node.left == null && node.right == null) {
        leaves.add(node.val);
    }
InOrder(node.left, leaves);
InOrder(node.right, leaves);
}
        
    }
