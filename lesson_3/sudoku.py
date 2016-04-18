def check_sudoku(p):
  n = len(p) #extract size of grid
  digit = 1 # start with 1
  while digit <=n: # go through each digit
    i = 0
    while i < n: # go through each rwo and column
      row_count = 0
      col_count = 0
      j = 0
      while j < n: #for each entry in it row/column
        if p[i][j] == digit: #check row count
          row_count = row_count + 1
        if p[j][i] == digit:
          col_count = col_count + 1
        j = j + 1
      if row_count != 1 or col_count != 1:
        return False
      i = i + 1 # next row/column
    digit = digit + 1 # next digit
  return True
