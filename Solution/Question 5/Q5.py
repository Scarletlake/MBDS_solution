# Q5


# Sort dictionary by the value
# Return the color of the bead left most
def rank_dict(beads_dict):
    ranked_beads = sorted(beads_dict.items(), key = lambda b:(b[1], b[0]), reverse=True)
    beads_dict = dict(ranked_beads)    
    return ranked_beads



# Fill the grid with a color
def fill_grid(grid, loc, color, beads):    
    grid[loc[0]][loc[1]] = color
    
    # Reduce the number of that color by 1
    # If no beads left, delete it from list
    beads[color] -= 1
    if beads[color] == 0:
        del beads[color]
    
    


# Find the beads that has different color to its neighbour and left most
def find_next_color(size, grid, loc, beads):  
    ranked_beads = rank_dict(beads)
    next_color = 0
    
    # 4 neighbors: up, right, down, left
    neighbors = [(loc[0]-1, loc[1]), (loc[0], loc[1]-1), (loc[0]+1, loc[1]), (loc[0], loc[1]+1)]  

    for color in ranked_beads:      
       
        has_duplic = 0
        
        for neighbor_loc in neighbors:            
            # location out of grid
            if (neighbor_loc[0] < 0 or neighbor_loc[0] >= size or    
                neighbor_loc[1] < 0 or neighbor_loc[1] >= size ):
                continue

            # color is the same
            elif grid[neighbor_loc[0]][neighbor_loc[1]] == color[0]:                
                has_duplic += 1                

            # color is different
            else:
                continue
        
        if has_duplic == 0:
            next_color = color[0]
            break  
        

    # if there is no differnet color
    if next_color == 0:
        next_color = ranked_beads[0][0]
        
    return next_color      
        
                

            
# Find the next color to fill the grid
def distribute_bead(grid, size, beads):
    # Fill the empty grid 
    for i in range(size):
        for j in range(size):
            # Fill the empty grid
            if grid[i][j] == 0:                         
                # find the next beads to fill                
                color = find_next_color(size, grid, (i, j), beads)                
                fill_grid(grid, (i, j), color, beads);

            else:
                pass



# fill the edge with a certain color
def fill_corner(size, grid, amount, color, beads):
    for corner in [(0,0), (0,size-1), (size-1,0), (size-1, size-1)]:
        if amount == 0:
            return amount
        else:
            fill_grid(grid, corner, color, beads)
            amount -= 1
    return amount
        
    


# fill the edge with a certain color
def fill_edge(size, grid, amount, color, beads):
    
    # fill the first row    
    for i in range(1, size-1):
        if amount <= 0:
            return
        else:
            if grid[0][i] == 0:
                fill_grid(grid, (0, i), color, beads)
                amount -= 1
    
    # fill the right and left rows from top to bottom
    for i in range(1, size-1):

        # fill the left 
        if amount <= 0:
            return
        else:
            if grid[i][0] == 0:
                fill_grid(grid, (i, 0), color, beads)
                amount -= 1

        # fill the left 
        if amount <= 0:
            return
        else:
            if grid[i][size-1] == 0:
                fill_grid(grid, (i, size-1), color, beads)
                amount -= 1    
    
    # fill the last row
    for i in range(1, size-1):
        if amount <= 0:
            return
        else:
            if grid[size-1][i] != 0:
                fill_grid(grid, (size-1, i), color, beads)
                amount -= 1


    
    
# Given the size of the grid and the number of beads,
# find the grid configuration with least penalty
def find_configuration(size, beads, output_file_name):
    
    """
     beads : a dictionary storing the colors of beads and there numbers
    """
    
    # Create the 2d array repersenting the L*L grid, 0 means not filled
    grid =[] 
    for i in range(size): 
        col = [] 
        for j in range(size): 
            col.append(0) 
        grid.append(col)      
   
    # Find the max beads
    ranked_beads = rank_dict(beads)   
    
    if size % 2 == 0:       # even
        grid_half = (size*size // 2)
    else:                   # odd
        grid_half = (size*size // 2) + 1
        
    # if the maximum number of beads is smaller than the half of the grid
    # then beads can be distributed without penalty  
    if ranked_beads[0][1] - grid_half >= 0:
        diff = ranked_beads[0][1] - (size*size - ranked_beads[0][1])
        
        # Fill the corners first
        diff = fill_corner(size, grid, diff, ranked_beads[0][0], beads)
            
        # Then fill the edge           
        fill_edge(size, grid, diff, ranked_beads[0][0], beads)
        

    # Fill the rest of the grid
    distribute_bead(grid, size, beads)

    # Print the result to output file
    f = open(output_file_name, "w")
    for i in range(size):
        for j in range(size):
            f.write(grid[i][j] + " ")
            
        f.write("\n")
        
    f.close()


                



""" Run the code for question5 """

""" Q5_2 """

size_1 = 5
colors_1 = {"R" : 12, "B" : 13}

find_configuration(size_1, colors_1, "output_question_5_1")

""" Q5_2 """

size_2 = 64
colors_2 = {"R" : 139, "B": 1451, "G" : 977, "W" : 1072, "Y" : 457}

find_configuration(size_2, colors_2, "output_question_5_2")




