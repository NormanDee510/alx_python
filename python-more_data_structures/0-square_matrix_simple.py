def square_matrix_simple(matrix=[]):   
    result = []   
    for row in matrix:      
        squared_row = []        
        
        for num in row:            
            squared_row.append(num ** 2)        
        result.append(squared_row)    
    return result