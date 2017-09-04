class Solution(object):
    """
    You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
    Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
    and there is exactly one island (i.e., one or more connected land cells).
    The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
    One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
    Determine the perimeter of the island.
    """
    def get_island_perimeter(self, grid):
        perimeter = 0
        crossing_sides = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    perimeter += 1

                    if i != 0 and grid[i-1][j] == 1:
                        crossing_sides += 1

                    if i != 0 and grid[i][j-1] == 1:
                        crossing_sides += 1

        return (4*perimeter)-(2*crossing_sides)


if __name__ == "__main__":
    sol = Solution()
    print(sol.get_island_perimeter([[0, 1, 0, 0],
                                    [1, 1, 1, 0],
                                    [0, 1, 0, 0],
                                    [1, 1, 0, 0]]))
