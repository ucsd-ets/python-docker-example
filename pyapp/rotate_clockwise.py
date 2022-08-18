from typing import List

def rotate_clockwise(matrix: List[List[int]]) -> None:
    """
    Rotate a nxn 2D int matrix 90 degrees clockwise in place

    Args:
        matrix: A nxn 2D int matrix
    
    Returns:
        matrix being roated 90 degree clockwise in place

    Raises:
        TypeError: If the matrix is not nxn 2D matrix
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix argument is not a List.")
    elif not isinstance(matrix[0], list):
        raise TypeError("matrix argument is not a 2D List")
    elif not len(matrix) == len(matrix[0]):
        raise TypeError("matrix argument is not a sqaure 2D List")

    n = len(matrix)
    # idea: first reflect along the main diagonal, then reflect along y-axis
    for i in range(1, n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        for j in range(n//2):
            matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]

    return