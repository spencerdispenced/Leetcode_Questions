package DSA_Problems.ArrayHashing.EncodeDecodeStrings;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class EncodeDecode {

    public static String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder();

        for (String str : strs) {
            encoded.append(str.length()).append("#").append(str);
        }

        return encoded.toString();
    }

    public static List<String> decode(String str) {
        List<String> decoded = new ArrayList<>();

        int i = 0;
        while (i < str.length()) {
            int j = i;

            while (str.charAt(j) != '#')
                j++;

            int length = Integer.valueOf(str.substring(i, j));

            i = j + 1 + length;

            decoded.add(str.substring(j + 1, i));
        }

        return decoded;
    }

    public static void main(String[] args) {
        List<String> strs = Arrays.asList("lint", "code", "love", "you");

        String encoded = encode(strs);
        System.out.println(encoded);

        List<String> decoded = decode(encoded);

        System.out.println(decoded);

    }
}
