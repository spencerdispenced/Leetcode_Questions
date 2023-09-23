package DSA_Problems.ArrayHashing.LongestPrefix;

public class LongestPrefix {

    public static String findLongestPrefix(String[] strs) {
        StringBuilder res = new StringBuilder();

        for (int i = 0; i < strs[0].length(); i++) {
            for (String string : strs) {
                if (i == string.length() || string.charAt(i) != strs[0].charAt(i)) {
                    return res.toString();
                }
            }
            res.append(strs[0].charAt(i));
        }
        return res.toString();
    }

    public static void main(String[] args) {
        String[] strs = {"flower","flow","flight"}; // fl
        String[] strs2 ={"dog","racecar","car"}; // ""
        System.out.println(findLongestPrefix(strs));
        System.out.println(findLongestPrefix(strs2));
        
    }
}
