# Q4
# Using 4-connectivity

# Read the input file and return a matrix as 2d array
def read_matrix(file_name):
    row = 0
    input_image = []
    input_file = open(file_name)
    
    for line in input_file.readlines():
        # [cluster_num, labled]
        if line.strip():
            input_image.append([ [int(i), 0] for i in line.split()])                 
        
    input_file.close()
    return input_image



# Find the cluster to which a pixel is connectd 
def find_cluster(loc, input_image, row, col):
    input_image[loc[0]][loc[1]][1] = 1        # Mark it as labeld

    # 4 neighbors: up, right, down, left pixels
    neighbors = [(loc[0]-1, loc[1]), (loc[0], loc[1]-1), (loc[0]+1, loc[1]), (loc[0], loc[1]+1)]
  
    
    for neighbor_loc in neighbors:
     
        # location out of boundary
        if (neighbor_loc[0] < 0 or neighbor_loc[0] >= row or    
            neighbor_loc[1] < 0 or neighbor_loc[1] >= col ):
            pass
             

        # terminate if it not connect to a new pixel
        elif (input_image[neighbor_loc[0]][neighbor_loc[1]][0] == 0 or      
              input_image[neighbor_loc[0]][neighbor_loc[1]][1] == 1 ):
            pass
        
        # if it connects new clusters
        # label this pixel and final new neighbours by recursively call this function
        else:           
            input_image[neighbor_loc[0]][neighbor_loc[1]][0] = input_image[loc[0]][loc[1]][0] # Lable the cluster number
            find_cluster(neighbor_loc, input_image, row, col);    
           

    
# Label all the clusters
def label_cluster(input_image, row, col):
    cluster_num = 0;
    
    for i in range(col):             
        for j in range(row):
            
            if input_image[j][i][1] == 0:       # if it is not labeled                      
               
                if input_image[j][i][0] == 0:       # no pixel
                    input_image[j][i][1] = 1        # Mark it as labeld
                    pass        
                
                else:
                    cluster_num += 1
                    input_image[j][i][0] = cluster_num      # find new cluster
                    find_cluster((j, i), input_image, row, col)
                    
                    
            
                
           
# Print the labeled image to the output file
def output_image(input_image, row):
   
    f = open("output_question_4", "w")
    for i in range(row):
        for pixel in input_image[i]:
            f.write(str(pixel[0]) + " ")
            
        f.write("\n")
        
    f.close()
    
    


# Find the connected components using 4-connectivity
def label_cluster_4_con(file_name):
    input_image = read_matrix(file_name)
    label_cluster(input_image, len(input_image), len(input_image[0]))   
    output_image(input_image, len(input_image))
             


""" Run the code for question4 """

label_cluster_4_con("input_question_4")
