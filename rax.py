def generate_knapsack_candidates(sublists, capacity):

  candidates = []

  def generate_knapsack_candidates_helper(remaining_sublists, remaining_capacity, current_subset):

    if remaining_capacity == 0:
      candidates.append(current_subset)
      return

    for i in range(len(remaining_sublists)):
      sublist = remaining_sublists[i]
      if sublist[1] <= remaining_capacity:
        # Add the sublist to the current_subset.
        new_subset = current_subset + [sublist]

        # Recursively generate all possible subsets of the remaining_sublists with the reduced capacity.
        generate_knapsack_candidates_helper(remaining_sublists[:i] + remaining_sublists[i + 1:], remaining_capacity - sublist[1], new_subset)

  generate_knapsack_candidates_helper(sublists, capacity, [])

  return candidates

sublists = [(1, 5), (2, 3), (3, 6)]
capacity = 11

# Generate all possible subsets of sublists that are less than or equal to the capacity.
candidates = generate_knapsack_candidates(sublists, capacity)

# Evaluate each candidate and return the best solution.
best_subset = None
best_value = 0
for candidate in candidates:
  value = sum([sublist[1] for sublist in candidate])
  if value > best_value:
    best_subset = candidate
    best_value = value

# Print the best solution.
print(best_subset)