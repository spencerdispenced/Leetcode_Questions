package DSA_Problems.ArrayHashing.GroupAnagrams;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class GroupAnagram {

    public static List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();

        if (strs.length == 0)
            return res;

        HashMap<String, List<String>> map = new HashMap<>();

        for (String s : strs) {
            char[] count = new char[26];

            for (char c : s.toCharArray()) {
                count[c - 'a']++;
            }

            String key = new String(count);
            map.computeIfAbsent(key, k -> new ArrayList<>());
            map.get(key).add(s);
        }

        res.addAll(map.values());

        return res;
    }

    public static void main(String[] args) {
        String[] strs = { "eat", "tea", "tan", "ate", "nat", "bat" };

        System.out.println(groupAnagrams(strs)); // [["bat"],["nat","tan"],["ate","eat","tea"]]
    }
}
