package DSA_Problems.SlidingWindow.PermutationsInAString;

import java.util.Arrays;

public class StringPerms {

    public static boolean permInString(String s1, String s2) {
        /*
         * Runtime 7 ms Beats 50.38%
         * Memory 42.9 MB Beats 15.85%
         */

        if (s1.length() > s2.length())
            return false;

        int s1Count[] = new int[26];
        int s2Count[] = new int[26];

        // Get counts for initial window
        for (int i = 0; i < s1.length(); i++) {
            s1Count[s1.charAt(i) - 'a']++;
            s2Count[s2.charAt(i) - 'a']++;
        }

        int left = 0;
        for (int right = s1.length(); right < s2.length(); right++) {
            if (Arrays.equals(s1Count, s2Count))
                return true;

            s2Count[s2.charAt(right) - 'a']++;
            s2Count[s2.charAt(left) - 'a']--;
            left++;
        }

        return Arrays.equals(s1Count, s2Count);
    }

    public static boolean permInStringOptimized(String s1, String s2) {
        /*
         * Runtime 8 ms Beats 46.7%
         * Memory 42.6 MB Beats 30.80%
         */
        if (s1.length() > s2.length())
            return false;

        int s1Count[] = new int[26];
        int s2Count[] = new int[26];

        // Get counts for initial window
        for (int i = 0; i < s1.length(); i++) {
            s1Count[s1.charAt(i) - 'a']++;
            s2Count[s2.charAt(i) - 'a']++;
        }

        // Get initial counts
        int matches = 0;
        for (int i = 0; i < s1Count.length; i++) {
            if (s1Count[i] == s2Count[i])
                matches++;
        }

        int left = 0;
        for (int right = s1.length(); right < s2.length(); right++) {
            if (matches == 26)
                return true;

            // Increment count of newly added char
            int index = s2.charAt(right) - 'a';
            s2Count[index]++;

            // Check if incrementing created a match
            if (s1Count[index] == s2Count[index])
                matches++;

            // Check if incrementing undid an existing match
            else if (s1Count[index] + 1 == s2Count[index])
                matches--;

            // Decrement count leaving window
            index = s2.charAt(left) - 'a';
            s2Count[index]--;

            // Check if decrementing created a match
            if (s1Count[index] == s2Count[index])
                matches++;

            // Check if decrementing undid an existing match
            else if (s1Count[index] - 1 == s2Count[index])
                matches--;

            left++;
        }

        return matches == 26;
    }

    public static void main(String[] args) {
        String str1 = "ab";
        String test1 = "eidbaooo"; // True
        String test2 = "eidboaoo"; // false

        String str2 = "hello";
        String test3 = "ooolleoooleh"; // False

        String str3 = "hello";
        String test4 = "ooollehooleh"; // True

        // System.out.println(permInString(str1, test1));// True
        // System.out.println(permInString(str1, test2));// False
        // System.out.println(permInString(str2, test3));// False
        // System.out.println(permInString(str3, test4));// True

        System.out.println(permInStringOptimized(str1, test1)); // True
        System.out.println(permInStringOptimized(str1, test2)); // False
        System.out.println(permInStringOptimized(str2, test3)); // False
        System.out.println(permInStringOptimized(str3, test4));// True
    }
}