
package DSA_Problems.SlidingWindow.MaxWithoutRepeats;

import java.util.HashSet;

public class MaxWithoutRepeats {

    public static int longestSubstring(String str) {
        int left = 0;
        int maxSub = 0;
        HashSet<Character> chars = new HashSet<>();

        for (int right = 0; right < str.length(); right++) {

            while (chars.contains(str.charAt(right))) {
                chars.remove(str.charAt(left));
                left++;

            }
            chars.add(str.charAt(right));
            maxSub = Math.max(maxSub, chars.size());
        }

        return maxSub;
    }

    public static void main(String[] args) {
        String s1 = "abcabcbb";
        String s2 = "bbbbb";
        String s3 = "pwwkew";
        String s4 = "aab";

        System.out.println(longestSubstring(s1)); // 3
        System.out.println(longestSubstring(s2)); // 1
        System.out.println(longestSubstring(s3)); // 3
        System.out.println(longestSubstring(s4)); // 2

    }
}