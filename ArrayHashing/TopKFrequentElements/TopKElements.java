
package DSA_Problems.ArrayHashing.TopKFrequentElements;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

// Given an integer array nums and an integer k,
//  return the k most frequent elements. You may return the answer in any order.

public class TopKElements {

    public static int[] topKFrequent(int[] nums, int k) {
        
        HashMap<Integer, Integer> count = new HashMap<>();
        List<Integer> buckets[]  = new ArrayList[nums.length + 1]; 

        for (int num : nums)
            count.merge(num, 1, Integer::sum);

        for (int key : count.keySet()){
            int freq = count.get(key);
            if (buckets[freq] == null)
                buckets[freq] = new ArrayList<>();
            buckets[freq].add(key);
        }

        int idx = 0;
        int[] ret = new int[k];
        for (int i = nums.length; i >= 0; i--) {
            if (buckets[i] != null) {
                for (int val : buckets[i]) {
                    ret[idx++] = val;
                    if (idx == k)
                        return ret;
                }
            }
        }

        return ret;
    }

    public static void main(String[] args) {
        int[] nums = {1,1,1,2,2,3};
        int k = 2; // [1,2]

        int[] nums2 = {1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3};
        int k2 = 2;
        
    
        int[] nums3 = {1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3};
        int k3 = 2;
        
        int[] f1 = topKFrequent(nums, k);
        int[] f2 = topKFrequent(nums2, k2);
        int[] f3 = topKFrequent(nums3, k3);
        

        System.out.println(Arrays.toString(f1));
        System.out.println(Arrays.toString(f2));
        System.out.println(Arrays.toString(f3));
    }
}
