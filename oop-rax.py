class Knapsack:
    def __init__(self, sublists, capacity):
        self.sublists = sublists
        self.capacity = capacity
        self.best_subset = None
    
    def generate_knapsack_candidates(self):
        candidates = []

        def generate_knapsack(remaining_sublists, remaining_capacity, current_subset):
            if remaining_capacity == 0:
                candidates.append(current_subset)
                return
            for i in range(len(remaining_sublists)):
                sublist = remaining_sublists[i]
                if sublist[1] <= remaining_capacity:
                    new_subset = current_subset + [sublist]
                    generate_knapsack(remaining_sublists[:i] + remaining_sublists[i + 1:], remaining_capacity - sublist[1], new_subset)
        generate_knapsack(self.sublists, self.capacity, [])
        return candidates
    
    def candidate_evaluation(self, candidate_subset):
        value = sum([sublist[1] for sublist in candidate_subset])
        return value
    
    def find_best(self):
        best_subset = None
        best_value = 0
        candidates = self.generate_knapsack_candidates()
        for candidate in candidates:
            value = self.candidate_evaluation(candidate)
            if value > best_value:
                best_subset = candidate
                best_value = value

        self.best_subset = best_subset
        
        return best_subset

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
        
        knapsack = Knapsack(sublists, capacity)
        best_subset = knapsack.find_best()

        #find the sum of the first index of everysublist in best_subset
        if best_subset == None:
            total_value = 0
        else: total_value = sum([sublist[1] for sublist in best_subset])

        
        print(f'Sum of the values: {total_value}')
        print(str(best_subset) + '\n\n')