package DSA_Problems.ArrayHashing.TwoSum;

import java.util.HashMap;

// https://leetcode.com/problems/two-sum/S

public class TwoSum {

    // Same as find_indexes but using HashMap

    public static int[] findTwoSum(int[] nums, int target) {
        // int[] ret = new int[2];

        // for (int i = 0; i < nums.length; i++) {
        // for (int j = i+1; j < nums.length; j++) {
        // if ((nums[i] + nums[j]) == target) {
        // ret[0] = i;
        // ret[1] = j;
        // }
        // }
        // }

        // return ret;

        HashMap<Integer, Integer> ret = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];

            if (ret.containsKey(nums[i])) {
                return new int[] { ret.get(num), i };
            }

            ret.put(target - num, i);
        }

        return new int[] {};

    }

    public static void printTwoSum(int[] arr) {
        System.out.print("[" + arr[0] + "," + arr[1] + "]\n");

    }

    public static void main(String[] args) {
        int[] arr1 = { 2, 7, 11, 15 };
        int[] arr1Ret = findTwoSum(arr1, 9);

        printTwoSum(arr1Ret);

        int[] arr2 = { 5, 7, 11, 15 };
        int[] arr2Ret = findTwoSum(arr2, 18);

        printTwoSum(arr2Ret);
    }
}
