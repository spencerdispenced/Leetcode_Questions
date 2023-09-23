package DSA_Problems.Graphs.FindTheIslands;

public class runner {
    static char[][] grid = { { '1', '1', '1', '1', '0' }, { '1', '1', '0', '1', '0' }, { '1', '1', '0', '0', '0' },
            { '0', '0', '0', '0', '0' } };

    public static void main(String[] args) {
        FindTheIslands2 t1 = new FindTheIslands2();
        System.out.println(t1.numIslands(grid));
    }
}
