## question 4
For the purpose of this question, functions to find clusters by 4-connectivity is implemented. 


The image is stored as a 2d array, each element is a list `[cluster_num, labled]` contains the cluser number of the pixel and if it is labeld.
labled == 0 means not labled, labled == 1 means it is labled.


To find the cluster the pixel belongs to, function `find_cluster` is called recursively. It will terminate if if it not connect to a pixel or it's neighbors is allready labled.


```python
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

```

