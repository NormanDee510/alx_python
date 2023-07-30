def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    squared_matrix = []
    
    # Iterate through each row in the input matrix
    for row in matrix:
        # Create a new row to store the squared values of the current row
        squared_row = []
        
        # Iterate through each element in the current row
        for element in row:
            # Calculate the square value and add it to the squared_row
            squared_row.append(element ** 2)
        
        # Add the squared_row to the squared_matrix
        squared_matrix.append(squared_row)
    
    return squared_matrix