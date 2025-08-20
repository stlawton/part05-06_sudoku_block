def block_correct(sudoku: list, row_no: int, column_no: int):
  checked_numbers = []
  number = 1
  while number < 10:
    for i in range(row_no, row_no + 3):
      for j in range(column_no, column_no + 3):
        if number == sudoku[i][j]:
          if checked_numbers.count(number) < 1:
            checked_numbers.append(number)
          else:
            return False
    number += 1
  return True
