def block_correct(sudoku: list, row_no: int, column_no: int):
  checked_numbers = []
  current_row = row_no
  while current_row < row_no + 3:
    number = 1
    long_row = sudoku[current_row]
    while number < 10:
      short_row = long_row[column_no : column_no + 3]
      if number in short_row:
        if checked_numbers.count(number) < 2:
          checked_numbers.append(number)
        else:
          return False
      number += 1
    current_row += 1
  return True
