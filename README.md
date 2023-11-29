# CPSC 335 Project 2
## Collaborators
- Jacob Corletto jacob.corletto@gmail.com

- Raxel Ortiz raxelortiz7@csu.fullerton.edu

- Helen Truong 

- Esteban Zapata eazapata@csu.fullerton.edu



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

### Usage

To use the code, first save it to a file named `Part-A.py`. Then, run the following command from a terminal:

```python Part-A.py```

This will read the input from the `input.txt` file and write the output to the `exhaustive_output.txt` file.


# Part-B 

Part-B of this project Stock Maximization in Dynamic Programming

This code implements a dynamic programming algorithm to solve the stock maximization problem. The problem is to find the subset of stocks that maximizes the total value of the stocks, given a budget constraint.

The `dp_max_stock` function takes three arguments:

* `my_list`: The list of stocks, where each stock is represented by a tuple of two integers: the index of the stock and the value of the stock
* `capacity`: The maximum budget
* `total_sublists`: The total number of stocks to consider

The function first checks if the base case is reached, either when there are no more stocks or the budget is exhausted. In either case, the function returns 0.

Next, the function checks if the value of the current stock exceeds the remaining budget. If it does, then the function recursively calls itself to consider the next stock without including the current stock. Otherwise, the function recursively calls itself to consider both including and excluding the current stock, and then returns the maximum of the two results.

### Input Format

The input to the code is a text file named `input.txt`. The file should contain one test case per line. Each test case should be formatted as follows:


```
total_sublists
my_list
capacity
```

where:

- `total_sublists` is an integer that specifies the total number of stocks to consider
- `my_list` is a list of stocks, where each stock is represented by a tuple of two integers: the index of the stock and the value of the stock
- `capacity` is an integer that specifies the maximum budget

### Output Format

The output of the code is a text file named `dp_output.txt`. The file should contain one output per test case. Each output should be formatted as follows:

```
Case #test_case_count
Total Stocks: max_sum
--------------------------------------------------
```

Where:

- `test_case_count` is the index of the test case
- `max_sum`is the maximum total value of stocks found

### Usage

To use the code, first save it to a file named `Part-B.py`. Then, run the following command from a terminal:

```python Part-B.py```

This will read the input from the `input.txt` file and write the output to the `dp_output.txt` file.