##  Question 5

* If the beads with maximum amount has is not more than half of the grids, then all beads can be distribbuted without penalty by selecting the color that is different to its neighbors with maximum amount left each time.
* However, If the beads with maximum amount has is more than half of the grids, the configuration with no penalty can not be found. To achieve the least penalty, put the redundant beads should be put into the corners first as grids in corners only have two neighbors. Then put the redundant beads into the grids along the edge as they only have three neighbors. Then fill the rest of the grid by selecting the color that is different to its neighbors with maximum amount left each time.

``` python
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

```
