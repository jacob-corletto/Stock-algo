#knapsack in dynamic programming
def knapSack(items, w, n):
    if n == 0 or w == 0:
        return 0
    if (items[n-1][1] > w):
        return knapSack(items, w, n-1)
# Driver program to test above function
    else:
        return max(items[n-1][1] + knapSack(items, w-items[n-1][1], n-1), knapSack(items, w, n-1))


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
                max_sum = knapSack(my_list, capacity, total_sublists)
                #sum of indexes of the sublists
                output_file.write("Case #" + str(test_case_count) + '\n')
                output_file.write("Value: " + str(max_sum) + '\n')
                output_file.write("--------------------------------------------------\n\n")

            total_sublists = 0
            my_list = []
            capacity = 0

            # Update the index to skip the processed lines
            i += 4
            test_case_count += 1
        else:
            i += 1  # Move to the next line








