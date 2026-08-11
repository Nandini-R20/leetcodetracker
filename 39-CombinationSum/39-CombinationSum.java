// Last updated: 8/11/2026, 12:26:40 PM
class Solution {

    List<List<Integer>> ans = new ArrayList<>();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {

        solve(candidates, target, 0, new ArrayList<>());
        return ans;
    }

    void solve(int[] arr, int target, int index, List<Integer> list) {

        if (target == 0) {
            ans.add(new ArrayList<>(list));
            return;
        }

        if (target < 0) {
            return;
        }

        for (int i = index; i < arr.length; i++) {

            list.add(arr[i]);              // Choose

            solve(arr, target - arr[i], i, list); // Reuse same number

            list.remove(list.size() - 1);  // Backtrack
        }
    }
}