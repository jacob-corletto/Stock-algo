#importing itertools for generating all possible combinations of sublists
import itertools

# Generate all possible combinations of sublists
def generate_combinations(total_sublists, list, capacity):
    best_sum = 0
    best_combination = []
    for r in range(1, total_sublists + 1):
        combinations = itertools.combinations(list, r)
        
        # Iterate through each combination
        for combination in combinations:
            current_sum = sum(sublist[1] for sublist in combination)
            current_capacity = sum(sublist[1] for sublist in combination)
            
            # Check if current_sum exceeds max_sum and satisfies capacity constraint
            if current_sum > best_sum and current_capacity <= capacity:
                best_sum = current_sum
                best_combination = combination

        # Check if the sum of the first values exceeds the capacity
        if sum(sublist[1] for sublist in best_combination) > capacity:
            best_sum = 0
            best_combination = []

    return best_sum, best_combination
    
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
                output_file.truncate()
                max_sum, max_combination = generate_combinations(total_sublists, my_list, capacity)
                #sum of indexes of the sublists
                total_stocks = sum(sublist[0] for sublist in max_combination)
                output_file.write("Case #" + str(test_case_count) + '\n')
                output_file.write("Value: " + str(max_sum) + '\n')
                output_file.write("Best combinations: " + str(max_combination) + '\n')
                output_file.write("Total Stocks: " + str(total_stocks) + '\n\n')
                output_file.write("--------------------------------------------------\n\n")

            total_sublists = 0
            my_list = []
            capacity = 0

            # Update the index to skip the processed lines
            i += 4
            test_case_count += 1
        else:
            i += 1  # Move to the next line




