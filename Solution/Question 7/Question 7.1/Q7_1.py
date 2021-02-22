#Q7_1



# Read coordinates from input file
def read_coordinates(co_file_name):
    coordinates = []
    input_file = open(co_file_name)
    
    for line in input_file.readlines()[1:]:
        if line.strip():
           coordinates.append((int(line.split()[0]), int(line.split()[1])))          
        
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
def coordinate_to_index(col, row, co_file_name, output_file_name):
    coordinates = read_coordinates(co_file_name)
    output_file = open(output_file_name, "w")
    output_file.write("index\n")
    
    for coordinate in coordinates:
        # Convert coordinate to cooresponding index
        index = coordinate[0] + coordinate[1]*col
        output_file.write(str(index) + "\n")

    output_file.close()



# Function to convert given index to coordinates
def index_to_coordinate(col, row, id_file_name, output_file_name):
    index_list = read_index(id_file_name)
    output_file = open(output_file_name, "w")
    output_file.write("x1\tx2\n")
    
    for index in index_list:
        # Convert index to cooresponding coordinate
        output_file.write(str(index % col) + "\t" + str(index // col) + "\n")

    output_file.close()

    
    

""" Run the code for question7_1 """

coordinate_to_index(50, 57, "input_coordinates_7_1.txt", "output_index_7_1.txt")

index_to_coordinate(50, 57, "input_index_7_1.txt", "output_coordinates_7_1.txt")
