
package DSA_Problems.TwoPointers.ThreeSum;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSum {

    public static List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> ret = new ArrayList<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int left = i + 1;
            int right = nums.length - 1;

            while (left < right) {
                int currSum = nums[left] + nums[right] + nums[i];

                if (currSum > 0)
                    right--;
                else if (currSum < 0)
                    left++;
                else {
                    ret.add(Arrays.asList(nums[i], nums[left], nums[right]));

                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }

                    left++;
                }
            }
        }

        return ret;
    }

    public static void main(String[] args) {
        int[] nums1 = { -1, 0, 1, 2, -1, -4 }; // [[-1,-1,2],[-1,0,1]]

        int[] nums2 = { 0, 1, 1 }; // []

        int[] nums3 = { 0, 0, 0 }; // [[0,0,0]]

        int[] nums4 = { -3, 3, 4, -3, 1, 2 }; // [[-3, 1, 2]]

        System.out.println(threeSum(nums1));
        System.out.println(threeSum(nums2));
        System.out.println(threeSum(nums3));
        System.out.println(threeSum(nums4));
    }
}