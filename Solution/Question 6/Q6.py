# Q6


# Read the points from the input file 
def read_points(file_name):
    points = []
    input_file = open(file_name)
    
    for line in input_file.readlines():
        if line.strip():
           points.append( (int(line.split()[0]), int(line.split()[1])))               
        
    input_file.close()
    return points



# Test if a ray intersects the edge of a polygon
def is_intersect(point, polygon_v1, polygon_v2):
    
    """
    Assume there is a ray coming out from the point from light to right
    """
    # The ray is parallel to the edge
    if polygon_v1[1] == polygon_v2[1]:
        return False
    
    # The ray is above the edge
    elif point[1] > polygon_v1[1] and point[1] >  polygon_v2[1]:
        return False

    # The ray is below the edge
    elif point[1] < polygon_v1[1] and point[1] <  polygon_v2[1]:
        return False

    # The ray is at the right of the edge
    elif point[0] > polygon_v1[0] and point[0] >  polygon_v2[0]:
        return False

    # The ray pass through one of or both the vertices, and it is below the edge
    elif ((point[1] == polygon_v1[1] and point[1] < polygon_v2[1]) or
          (point[1] == polygon_v2[1] and point[1] < polygon_v1[1])):
        return False
    
    # The ray pass through one of or both the vertices, and it is above the edge
    elif ((point[1] == polygon_v1[1] and point[0] <= polygon_v1[0] and point[1] > polygon_v2[1]) or
          (point[1] == polygon_v2[1] and point[0] <= polygon_v2[0] and point[1] > polygon_v1[1])):        
        return True
    
    # The ray is at the left of the edge and the point of intersection is at the right of the ray
    elif (point[0] <= polygon_v1[0] and point[0] <=  polygon_v2[0] and
          (polygon_v1[1] < point[1] < polygon_v2[1] or polygon_v1[1] > point[1] > polygon_v2[1]) ):        
        return True
    
    # The point of intersection is at the left of the ray
    # Consider the edge as a function, if the point is above the
    # line, then the ray does not intersect with the edge.
    # slop = (v1_x-v2_x)/(v1_y-v2_y)
    
    
    slop = (polygon_v1[0] - polygon_v2[0]) / (polygon_v1[1] - polygon_v2[1])
    start_v = polygon_v1
    end_v = polygon_v2
    if polygon_v1[0] > polygon_v1[1]:
        start_v = polygon_v2
        end_v = polygon_v1
        
    if slop *(point[0]-start_v[0]) > (point[1]-start_v[1]): # below the line
        if slop < 0:    
            return False
        else:
            return True


        



# Find out if the point is inside our outside the polygon
def test_location(points, polygon, output_file_name):             
    
    f = open(output_file_name, "w")
    
    # Test each point
    for point in points:
        intersect_num = 0
        for i in range(len(polygon)-1):           
    
            if is_intersect(point, polygon[i], polygon[i+1]):
                intersect_num += 1
        

        # Check if the number of intersection is odd number or even number
        # if odd, then inside, otherwise outside
        f.write(str(point[0]) + " " + str(point[1]) + " " + str(intersect_num)+ " ")
        if intersect_num % 2 == 1:
            f.write("inside\n")
        else:
            f.write("outside\n")
        
    f.close()
           

    

# Read the points and polygon vertices from input files
def test_point_location(file_name_points, file_name_polygon, output_file_name):    
    points = read_points(file_name_points)
    polygon = read_points(file_name_polygon)
    test_location(points, polygon, output_file_name)
    
    

""" Run the code for question6 """

test_point_location("input_question_6_points",
                    "input_question_6_polygon",
                    "output_question_6")
