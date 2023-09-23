package DSA_Problems.ArrayHashing.ValidAnagram;

import java.util.HashMap;

// https://leetcode.com/problems/valid-anagram/

public class ValidAnagram {

    public static boolean findAnagram(String s1, String s2) {

        /*
         * Add both strings to hashmaps with counters for each character, compare both
         * hashmaps
         */
        if (s1.length() != s2.length())
            return false;

        HashMap<Character, Integer> charCount1 = new HashMap<>();
        HashMap<Character, Integer> charCount2 = new HashMap<>();

        for (char c : s1.toCharArray()) {
            charCount1.put(c, charCount1.getOrDefault(c, 0) + 1);
        }

        for (char c : s2.toCharArray()) {
            charCount2.put(c, charCount2.getOrDefault(c, 0) + 1);
        }

        return charCount1.equals(charCount2);

    }

    public static void main(String[] args) {

        System.out.println(findAnagram("anagram", "nagaram")); // true
        System.out.println(findAnagram("rat", "cat")); // false
        System.out.println(findAnagram("apple", "epalp")); // true
        System.out.println(findAnagram("anagram", "nagarax")); // false

    }
}
