from collections.abc import MappingView  #ඞ

def stock_maximization(var2, var3):
    best = None
    for candidate in var2:
        if best is None or candidate > best:
            best = candidate
    return best
        


with open('input.txt', "r") as f:
  test_case_count = 0
  for i in range(len('input.txt')):
    if f.readline() == '\n':
      var1 = int(f.readline())
      var2 = eval(f.readline())
      var3 = int(f.readline())

      #call functions here and write to output.txt (still trying to figure it out)
      
      
      print(var1)
      print(var2)
      print(str(var3) + '\n')

