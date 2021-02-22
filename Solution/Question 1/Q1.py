# Q1


# Convert the steps into operations string
def operation_str(row, step_list):
    op_str = ""
    for i in range(row-1):
        op_str += "R"*step_list[i]        
        op_str += "D"

    return op_str + "R"*step_list[row-1]
        

# Find out the steps to abtain the sum
def find_operation(row, col, sum_num_list, output_file_name):

    output_file = open(output_file_name, "a")
    
    # Start from the min path
    # Use list to store the steps whose element are the number of right operation on that row
    steps = [col-1]
    steps.extend([0]*(row -1))  
    min_sum = sum(range(1,row+1)) + col - 1    

    for sum_num in sum_num_list:
        dif = sum_num - min_sum
        if dif == 0:   # Min path
            output_file.write(str(sum_num) + "R"*(col-1) + "D"*(row-1) + "\n")
        
        elif dif == (col-1)*(row-1):  # Max path
            steps[0] = 0
            steps[row-1] = col - 1
            output_file.write(str(sum_num) + "D"*(row-1) + "R"*(col-1) + "\n")
        
        elif dif < 0 or dif > (col-1)*(row-1): # No Results
            output_file.write(str(sum_num) + " no results\n")
                
        else:
            flag = row-1
            move = 0
            
            while dif > 0:
                move = dif // (flag)
                dif -= move * (flag)
                steps[0] -= move
                steps[flag] += move
                flag -= 1
                
            output_file.write(str(sum_num) + " " + operation_str(row, steps) + "\n")

    
    output_file.write("\n")
    
    # close file
    output_file.close()

    

""" Run the code for question1 """

""" Q1_a"""
find_operation(9, 9, [65, 72, 90, 110], "output_question_1")

""" Q1_b"""
find_operation(90000, 100000, [87127231192, 5994891682], "output_question_1")




