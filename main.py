def knapsack_best_subset_exhaustive(sublists, capacity):
  """Returns the best subset of sublists that maximizes the sum of the second values, subject to the given capacity.

  Args:
    sublists: A list of sublists, where each sublist is a list of two elements: the profit and weight of the sublist.
    capacity: The maximum capacity of the knapsack.

  Returns:
    The best subset of sublists that maximizes the sum of the second values, subject to the given capacity.
  """

  # Initialize the best subset and the maximum value.
  best_subset = []
  max_value = 0

  # Consider all possible subsets of the sublists.
  for i in range(1 << len(sublists)):
    subset = []
    total_weight = 0
    total_value = 0

    for j in range(len(sublists)):
      if (i >> j) & 1:
        subset.append(sublists[j])
        total_weight += sublists[j][1]
        total_value += sublists[j][0]

    # If the subset has a weight less than or equal to the capacity of the knapsack and a value greater than the current maximum value, update the best subset and the maximum value.
    if total_weight <= capacity and total_value > max_value:
      best_subset = subset
      max_value = total_value

  # Return the best subset.
  return best_subset


# Solve the knapsack problem.
sublists = [[1,2],[4,3],[3,6],[6,7]]
capacity = 12
best_subset = knapsack_best_subset_exhaustive(sublists, capacity)

# Print the maximum sum of the second values and the best subset.
print(sum([sublist[1] for sublist in best_subset]))
print(best_subset)
# print(str(var1) + '\n')
      
