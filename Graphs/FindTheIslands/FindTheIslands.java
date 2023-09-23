package DSA_Problems.Graphs.FindTheIslands;

class FindTheIslands {
    public int numIslands(char[][] grid) {
        int maxSize = 0;

        for (int row = 0; row < grid.length; row++) {
            for (int col = 0; col < grid[row].length; col++) {
                if (grid[row][col] == 1) {
                    int size = getIslandsSize(grid, row, col);
                    maxSize = maxSize > size ? maxSize : size;
                }
            }
        }
        return maxSize;
    }

    public int getIslandsSize(char[][] grid, int row, int col) {
        // Check for cells that are out of boundary
        if (row < 0 || col < 0 || row >= grid.length || col >= grid[row].length)
            return 0;

        // Check for the cells which have 0
        if (grid[row][col] == 0)
            return 0;

        // Mark cell as visited
        grid[row][col] = 0;

        // Apply DFS on adjacent cells
        int size = 1;
        for (int r = row - 1; r <= row + 1; r++) {
            for (int c = col - 1; c <= col + 1; c++) {
                // Exclude the current cell
                if (r != row || c != col)
                    size += getIslandsSize(grid, r, c);
            }
        }
        return size;
    }
}
