package DSA_Problems.ArrayHashing.MaxConseqSequence;

import java.util.HashSet;

public class MaxSequence {

    public static int findMaxSequence(int[] nums) {
        int maxSequence = 1;

        HashSet<Integer> numSet = new HashSet<>();

        for (int num : nums)
            numSet.add(num);

        for (int num : numSet) {
            if (!numSet.contains(num - 1)) {
                int sequence = 1;

                while (numSet.contains(num + sequence)) {
                    sequence++;
                }

                maxSequence = Math.max(sequence, maxSequence);
            }
        }

        return maxSequence;
    }

    public static void main(String[] args) {
        int[] nums = { 100, 4, 200, 1, 3, 2 };
        int[] nums2 = { 0, 3, 7, 2, 5, 8, 4, 6, 0, 1 };

        System.out.println(findMaxSequence(nums)); // 4
        System.out.println(findMaxSequence(nums2)); // 9
    }
}
