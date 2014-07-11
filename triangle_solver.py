"""
This file contains the function max_path_sum.

Given a text file with a triange of numbers, the function max_path_sum
returns the maximum sum of adjacent numbers along a path moving down the
triangle.

For example, by starting at the top of the triangle and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 27.

        5
      9   6
    4   6   8
  0   7   1   5

I.e. 5 + 9 + 6 + 7 = 27.
"""


def max_path_sum(filename):
    """
    Given the name of a file with space-separated integers in triangle format,
    finds the maximum sum of integers along any path going down the triangle,
    from each integer decending either leftwards or rightwards. For example,
    given a file:
                         2
                        3 8
                      12 9 7
    this method will return 19, since 2+8+9=19.

    @param filename: The name of the file with the triangle integer data
    @return:         The value of the maximum sum down any path
    """
    # Read the file into memory
    file = open(filename, 'r')
    try:
        triangle = _read_file_to_triangle(file)
    finally:
        file.close()

    # Calculate and return the max path sum
    return _calculate_max_path_sum(triangle)


def _read_file_to_triangle(file):
    """
    Read the contents of a file and store the integer values in a triangular
    dictionary of lists.

    @param file: The opened file with the properly formatted integer values
                 of a triangle. Each line of the file must represent a row
                 of the triangle, and must include only integers separated
                 by spaces.
    @return:     A dictionary, each key an integer representing the row of the
                 triangle, and each value a list of the integer values on that
                 row of the triangle.
    """
    # Initialize the triangle to be stored in memory.
    triangle = {}

    # Read lines in from the file one by one, and store them in the triangle.
    line_num = 1
    line = file.readline()
    while line:
        # Divide each line at the white space, and convert each value to an int
        triangle[line_num] = [int(number) for number in line.split()]

        # Confirm that the number of values in each line is correct
        if len(triangle[line_num]) != line_num:
            raise Exception("File is not formatted into a triangle")

        # Read the next line in the file
        line_num += 1
        line = file.readline()

    return triangle


def _calculate_max_path_sum(triangle):
    """
    Calculate the maximum sum of integers along any path through a triangular
    dictionary of lists. A path descends from the top of the triangle from
    each integer to the row below it, either to the left or to the right.

    @param triangle: A dictionary, each key an integer representing the row of
                     the triangle, and each value a list of the integer values
                     on that row of the triangle.
    @return:         The integer value of the maximum sum along any path down
                     the input triangle.
    """
    # Replace each position in the triangle with the maximum possible sum of a
    # path ending at that position, by adding the greater of the two values in
    # possible paths above it. In this way, we determine the sums cumulatively.
    for row_num in xrange(2, len(triangle) + 1):
        row = triangle[row_num]
        end_of_row = len(row) - 1
        row_above = triangle[row_num - 1]
        end_of_row_above = len(row_above) - 1
        for col in xrange(0, row_num):
            # The first and last position in each row has only one possible
            # path that reaches it. For the positions between, we take the
            # greater of the two possible paths.
            row[col] += (row_above[0] if col == 0 \
                     else row_above[end_of_row_above] if col == end_of_row \
                     else max(row_above[col - 1], row_above[col]))

    # The last row of the triangle now contains, in each position,
    # the maximum possible sum terminating in that position.
    # We return the largest of these values, the maximum possible
    # sum of any path through the triangle.
    return max(row)
