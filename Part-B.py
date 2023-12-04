#Stock Maximization in dynamic programming
def dp_max_stock(my_list, capacity, total_sublists):
    if total_sublists == 0 or capacity == 0:
        return 0 
    if (my_list[total_sublists-1][1] > capacity):
        return dp_max_stock(my_list, capacity, total_sublists-1) 
    else:
        return max(my_list[total_sublists-1][0] + dp_max_stock(my_list, capacity-my_list[total_sublists-1][1], total_sublists-1),  
        dp_max_stock(my_list, capacity, total_sublists-1)) 


with open('input.txt', "r") as f:
    test_case_count = 1
    lines = f.readlines()  # Read all lines into a list
    i = 0

    while i < len(lines):
        if lines[i] == '\n':
            total_sublists = int(lines[i + 1])
            my_list = eval(lines[i + 2])
            capacity = int(lines[i + 3])

            with open("dp_output.txt", "a") as output_file:
                output_file.truncate()
                max_sum = dp_max_stock(my_list, capacity, total_sublists)
                #sum of indexes of the sublists
                output_file.write("Case #" + str(test_case_count) + '\n')
                output_file.write("Total Stocks: " + str(max_sum) + '\n')
                output_file.write("--------------------------------------------------\n\n")

            total_sublists = 0
            my_list = []
            capacity = 0

            # Update the index to skip the processed lines
            i += 4
            test_case_count += 1
        else:
            i += 1  # Move to the next line








