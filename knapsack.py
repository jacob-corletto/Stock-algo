import itertools

total_sublists = 4
list = [[1,2],[4,3],[3,6],[6,7], [4,7]]
capacity = 10

# Generate all possible combinations of sublists
def exhuastive_method(total_sublists, list, capacity):
    max_sum = 0
    max_combination = []
    for r in range(1, total_sublists + 1):
        combinations = itertools.combinations(list, r)
        
        # Iterate through each combination
        for combination in combinations:
            current_sum = sum(sublist[1] for sublist in combination)
            current_capacity = sum(sublist[1] for sublist in combination)
            
            # Check if current_sum exceeds max_sum and satisfies capacity constraint
            if current_sum > max_sum and current_capacity <= capacity:
                max_sum = current_sum
                max_combination = combination

        # Check if the sum of the first values exceeds the capacity
        if sum(sublist[1] for sublist in max_combination) > capacity:
            max_sum = 0
            max_combination = []

    return max_sum, max_combination
    
with open('input.txt', "r") as f:
    test_case_count = 1
    lines = f.readlines()  # Read all lines into a list
    i = 0

    while i < len(lines):
        if lines[i] == '\n':
            total_sublists = int(lines[i + 1])
            my_list = eval(lines[i + 2])
            capacity = int(lines[i + 3])

            with open("exhaustive_output.txt", "a") as output_file:
                max_sum, max_combination = exhuastive_method(total_sublists, my_list, capacity)
                output_file.write("Case #" + str(test_case_count) + '\n')
                output_file.write(str(max_sum) + '\n')
                output_file.write(str(max_combination) + '\n\n')

            total_sublists = 0
            my_list = []
            capacity = 0

            # Update the index to skip the processed lines
            i += 4
            test_case_count += 1
        else:
            i += 1  # Move to the next line




