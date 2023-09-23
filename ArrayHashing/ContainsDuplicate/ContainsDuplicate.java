package DSA_Problems.ArrayHashing.ContainsDuplicate;

import java.util.HashSet;
import java.util.Set;

// https://leetcode.com/problems/contains-duplicate/

public class ContainsDuplicate {

    public static boolean containsDuplicate(int[] nums) {

        Set<Integer> uniques = new HashSet<Integer>();

        for (Integer i : nums) {
            if (uniques.contains(i))
                return true;
            else
                uniques.add(i);
        }

        return false;

    }

    public static void main(String[] args) {

        int[] nums = { 1, 2, 3, 1 }; // true
        int[] nums2 = { 1, 2, 3, 4 }; // false

        System.out.println(containsDuplicate(nums));
        System.out.println(containsDuplicate(nums2));

    }
}
