def knapsack_best_subset(sublists, capacity):
  
  # Sort the sublists in decreasing order of their second values.
  sublists.sort(key=lambda sublist: sublist[1], reverse=True)
  # print('first sort', sublists)
  # Initialize the final solution.
  final_solution = []
  total_weight = 0
  
  # Add sublists to the final solution until the capacity is exceeded.
  for sublist in sublists:
    if total_weight + sublist[1] <= capacity:
      final_solution.append(sublist)
      total_weight += sublist[1]
    else:
      break

  # Return the final solution.
  return final_solution

with open('input.txt', "r") as f:
  test_case_count = 0
  for i in range(len('input.txt')):
    if f.readline() == '\n':
      var1 = int(f.readline())
      sublists = eval(f.readline())
      capacity = int(f.readline())

      print(f'This size of input array {var1}')
      print(f'Stocks_and_Values {sublists}')
      print(f'this is the amount {capacity}')


      #call functions here and write to output.txt (still trying to figure it out)
      best_subset = knapsack_best_subset(sublists, capacity)

# Print the maximum sum of the second values and the best subset.
      print(sum([sublist[1] for sublist in best_subset]))
      print(best_subset)
      print(str(var1) + '\n')
      