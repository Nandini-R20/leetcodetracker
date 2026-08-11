// Last updated: 8/11/2026, 12:22:53 PM
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


// class Solution {
//     int[] seen = new int[10001]; 
//     int duplicate = -1;

//     public int[] findMode(TreeNode root) {
//         traverse(root);
//         return duplicate;
//     }

//     public void traverse(TreeNode node) {
//         if (node == null || duplicate != -1) return;

//         if (seen[node.val] == 1) {
//             duplicate = node.val;
//             return;
//         }

//         seen[node.val] = 1;

//         traverse(node.left);
//         traverse(node.right);
//     }
// }
    
  class Solution {
    List<Integer> result = new ArrayList<>();
    int currentCount = 0;
    int maxCount = 0;
    Integer prev = null;

    public int[] findMode(TreeNode root) {
        inOrder(root);
        int[] modeArray = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
       modeArray[i] = result.get(i);
        }
        return modeArray;
    }

    private void inOrder(TreeNode node) {
        if (node == null) return;

        inOrder(node.left);

        if (prev != null && node.val == prev) {
            currentCount++;
        } else {
            currentCount = 1;
        }

        if (currentCount > maxCount) {
         maxCount = currentCount;
        result.clear();
         result.add(node.val);
        } else if (currentCount == maxCount) {
            result.add(node.val);
        }

        prev = node.val;

        inOrder(node.right);
    }
}