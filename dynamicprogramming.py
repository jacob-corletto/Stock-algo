#knapsack in dynamic programming
def knapSack(items, w, n):
    if n == 0 or w == 0:
        return 0
    if (items[n-1][1] > w):
        return knapSack(items, w, n-1)
# Driver program to test above function
    else:
        return max(items[n-1][1] + knapSack(items, w-items[n-1][1], n-1), knapSack(items, w, n-1))

n = 4
items = [[1,2],[3,6],[4,3],[6,7]]
w = 12
print(knapSack(items, w, n))


