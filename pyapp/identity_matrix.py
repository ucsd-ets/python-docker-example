from typing import List

def is_square(matrix: List[List[int]]) -> bool: 

    """
    Checks if a given matrix is a square matrix

    Args:
        matrix: An mxn matrix 
    
    Returns:
        True if given matrix is square (m=n), otherwise False

    Raises:
        None
    """

    hight = len(matrix);

    for i in range(1, hight): 
        if len(matrix[i]) != hight:
            return False
    
    return True

def identity_matrix(matrix: List[List[int]]) -> List[List[int]]:

    """
    Takes in a matrix, and creates an identity matrix for it

    Args:
        matrix: An mxn matrix 
    
    Returns:
        an identity matrix of a given matrix  

    Raises:
        TypeError: If the matrix is not nxn 2D matrix
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix argument is not a List.")
    elif not isinstance(matrix[0], list):
        raise TypeError("matrix argument is not a 2D List")
    elif not is_square(matrix):
        raise TypeError("matrix argument is not a sqaure 2D List")


    height = len(matrix)
    
    return_matrix = []
    

    for i in range (0, height):
        return_matrix.append(list())

        for j in range (0, height):
            if i == j: 
                return_matrix[i].append(1)
            else: 
                return_matrix[i].append(0)

    return return_matrix

