package DSA_Problems.ArrayHashing.ValidSudoku;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class ValidSoduku {

    public static boolean isValidSoduku(char[][] board) {

        List<HashSet<Character>> rows = new ArrayList<>();
        List<HashSet<Character>> cols = new ArrayList<>();
        List<HashSet<Character>> squares = new ArrayList<>();

        for (int i = 0; i < 9; i++) {
            HashSet<Character> colSet = new HashSet<>();
            HashSet<Character> rowSet = new HashSet<>();
            HashSet<Character> squareSet = new HashSet<>();
            
            rows.add(rowSet);
            cols.add(colSet);
            squares.add(squareSet);
        }

        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[0].length; c++) {
                if (board[r][c] == '.') 
                    continue;
                
                if (
                    (!rows.get(r).add(board[r][c]) || 
                    (!cols.get(c).add(board[r][c]) || 
                    (!squares.get((r / 3) * 3 + (c / 3)).add(board[r][c]))))
                )
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        char[][] board = {
        {'5', '3', '.', '.', '7', '.', '.' , '.', '.'},
        {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
        {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
        {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
        {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
        {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
        };


    char[][] board2 = {
        {'8', '3', '.', '.', '7', '.', '.' ,'.', '.'},
        {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
        {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
        {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
        {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
        {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
        };

        System.out.println(isValidSoduku(board)); // true
        System.out.println(isValidSoduku(board2)); // false
    }
}
