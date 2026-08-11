// Last updated: 8/11/2026, 12:23:32 PM
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> map=new HashMap<>();
        for(int num:nums){
            map.put(num,map.getOrDefault(num,0)+1);
        }
        int[] arr=new int[k];
        for(int i=0;i<k;i++){
            int max=0;
            int max2=0;
            for(int key:map.keySet()){
                if(map.get(key)>max2){
                    max2=map.get(key);
                    max=key;

                }
            }
            arr[i]=max;
            map.remove(max);
        }
        return arr;
    
    }
}