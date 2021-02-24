## Question 6

To check if a point is inside a polygon, a ray is drawn from the point from left to right, if this ray intersects with edges of polygon for odd number of times, then it is inside the polygon.

The following situations should not be considered as intersection.
* The ray overlaps the edge
* The ray pass through one of the edge and it is below the edge

<p align="center">
  <img src="q6_1.jpg" height=500 >
</p>


```python
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
        return True# The ray is parallel to the edge
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
```


To test if the point of intersection is at the left or right of side of the ray, the edge is considered as a linear function where the vertices are the points on that line. For example, when slop > 0, if the testing point is above the line, then the ray does not intersect with the edge.

<p align="center">
  <img src="q6_2.jpg" height=300>
</p>

```python

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
            
```



