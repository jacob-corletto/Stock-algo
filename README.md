# CPSC 335 Project 2
## Collaborators
- Raxel Ortiz raxelortiz7@csu.fullerton.edu

- Jacob Corletto jacob.corletto@gmail.com

- Esteban Zapata eazapata@csu.fullerton.edu

- Helen Truong 


# Part-A

The Part-A of this project is an exhaustive implementation of the stock maximization.

The code first imports the `itertools` module, which provides functions for generating combinations of elements. The main part of the code is the `generate_combinations` function, which takes three arguments:

* `total_sublists`: The total number of sublists to consider
* `list`: The list of sublists
* `capacity`: The maximum capacity of the knapsack

The function first initializes two variables: `best_sum` and `best_combination`. These variables store the best sum and best combination of sublists found so far.

The function then iterates over all possible combinations of sublists, using the `itertools.combinations` function. For each combination, the function calculates the sum and capacity of the sublists. If the sum is greater than the current best sum and the capacity is less than or equal to the maximum capacity, then the sum and combination are updated.

Finally, the function returns the best sum and best combination.

### Input Format

The input to the code is a text file named `input.txt`. The file should contain one test case per line. Each test case should be formatted as follows:


- total_sublists
- my_list
- capacity


where:

* `total_sublists` is an integer that specifies the total number of sublists to consider
* `my_list` is a list of sublists, where each sublist is represented by a tuple of two integers: the index of the sublist and the value of the sublist
* `capacity` is an integer that specifies the maximum capacity of the knapsack

### Output Format

The output of the code is a text file named `exhaustive_output.txt`. The file should contain one output per test case. Each output should be formatted as follows:

```
Case #test_case_count
Value: max_sum
Best combinations: max_combination
Total Stocks: total_stocks
```
