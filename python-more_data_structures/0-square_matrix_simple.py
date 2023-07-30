def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    result = []
    
    # Iterate through each row in the input matrix
    for row in matrix:
        # Create a new row to store the squared values of the current row
        squared_row = []
        
        # Iterate through each element in the current row
        for num in row:
            # Square the value and append it to the new row
            squared_row.append(num ** 2)
        
        # Append the squared row to the result matrix
        result.append(squared_row)
    
    return result