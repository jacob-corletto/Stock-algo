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

    print("Maximum sum:", max_sum)
    print("Combination of sublists:", str(max_combination) + '\n')

with open('input.txt', "r") as f:
    test_case_count = 0
    for i in range(len('input.txt')):
        if f.readline() == '\n':
            total_sublists = int(f.readline())
            list = eval(f.readline())
            capacity = int(f.readline())

            exhuastive_method(total_sublists, list, capacity);

    


