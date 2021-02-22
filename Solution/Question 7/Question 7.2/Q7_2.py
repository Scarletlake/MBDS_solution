#Q7_2


# Read coordinates from input file
def read_coordinates(co_file_name):
    coordinates = []
    input_file = open(co_file_name)
    
    for line in input_file.readlines()[1:]:
        if line.strip():
           coordinates.append([ int(x) for x in line.split()])          
        
    input_file.close()
    
    return coordinates



# Read index from input file
def read_index(id_file_name):
    index = []
    input_file = open(id_file_name)
    
    for line in input_file.readlines()[1:]:
        if line.strip():
           index.append(int(line.split()[0]))
        
    input_file.close()
    
    return index



# Function to convert given coordinates to index
# I(x1, ... xn) = f1*x1 + ... fn*xn
def coordinate_to_index(size, co_file_name, output_file_name):
    dimension = len(size)
    coordinates = read_coordinates(co_file_name)
    output_file = open(output_file_name, "w")
    factors = [1] # f1 ... fn

    # write header
    output_file.write("index\n")    
   
    
    # compute the factors f1 ... fn
    for i in range(0,dimension-1):
        factors.append(factors[-1]*size[i])
        
    # Convert coordinate to cooresponding index
    for coordinate in coordinates:
        index = coordinate[0]        
        for i in range(1,dimension):          
            index += coordinate[i]*factors[i]            
        
        output_file.write(str(index) + "\n")
        
    output_file.close()

    

# Function to convert given index to coordinates
def index_to_coordinate(size, id_file_name, output_file_name):
    dimension = len(size)
    index_list = read_index(id_file_name)
    output_file = open(output_file_name, "w")
    factors = [1] # f1 ... fn
    coordinate = []
    remainder = 0
    
    # write header
    for i in range(1,dimension):            
        output_file.write("x" + str(i) + "\t")
        
    output_file.write("x" + str(dimension) + "\n")
   
    # compute the factors f1 ... fn
    for i in range(0,dimension-1):
        factors.append(factors[-1]*size[i])
    
    # Convert index to cooresponding coordinate   
    for index in index_list:
        remainder = index
        coordinate = []
        for i in range(1, dimension):            
            if remainder > 0:
                coordinate.append(remainder // factors[-i])
                remainder = remainder % factors[-i]
            else:
                coordinate.append(0)
                            
        # Print out the result
        output_file.write(str(remainder) + "\t")
        for i in range(1, dimension-1):            
            output_file.write(str(coordinate[-i]) + "\t")
            
        output_file.write(str(coordinate[0]) + "\n")
        
    output_file.close()
   
    

""" Run the code for question7_2 """

coordinate_to_index((4, 8, 5, 9, 6, 7), "input_coordinates_7_2.txt", "output_index_7_2.txt")

index_to_coordinate((4, 8, 5, 9, 6, 7), "input_index_7_2.txt", "output_coordinates_7_2.txt")
