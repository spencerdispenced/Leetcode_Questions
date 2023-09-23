package DSA_Problems.ArrayHashing.ProductOfArrayExceptSelf;

import java.util.Arrays;

class ProductOfArrayExceptSelf {

    public static int[] prodductOfArrXcptSelf(int[] nums) {
        int[] ret = new int[nums.length];
        Arrays.fill(ret, 0, ret.length, 1);

        int prefix = 1;
        int postfix = 1;


        for (int i = 0; i < nums.length; i++) {
            ret[i] = prefix;
            prefix *= nums[i];
        }

        for (int i = nums.length-1; i >= 0; i--) {
            ret[i] *= postfix;
            postfix *=nums[i];
        }

        return ret;
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4};
        int[] nums2 = {-1,1,0,-3,3}; 
        
        int[] ret1 = prodductOfArrXcptSelf(nums); 
        int[] ret2 = prodductOfArrXcptSelf(nums2);

        System.out.println(Arrays.toString(ret1)); // [24,12,8,6]
        System.out.println(Arrays.toString(ret2)); // [0,0,9,0,0]
        
    }
}