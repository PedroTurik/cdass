import os
from time import sleep
SQUARE = '\u2598'
BLANK = '\u2800'
BOARD_HEIGHT = 60
BOARD_WIDTH = 200

def get_matrix(alives, h, w):
   """
   Return a matrix of booleans, with given proportions
   where True means that index should be printed as SQUARE, and False as BLANK
   """
   matrix = [[0] * w for _ in range(h)]
   for y, x in alives:
      for k in range(y-1, y+2):
         for m in range(x-1, x+2):
            try:
               matrix[k][m] += 1
            except IndexError:
               pass

   ret_matrix = []
   for i, row in enumerate(matrix):
      new_row = []
      for j, cell in enumerate(row):
         if cell == 3:
            new_row.append(True)
         elif cell == 4 and (i, j) in alives:
            new_row.append(True)
         else:
            new_row.append(False)
      ret_matrix.append(new_row)
   return ret_matrix

#############################################

## Get input coordinates ##
alives = []
with open('coord.txt') as f:
   for row in f:
      if row.strip():
         alives.append(tuple(map(int, row.strip().split(','))))

#############################################




#############################################

## SETUP INITIAL STATE ##
os.system('clear')
for _ in range(5):
	os.system('xdotool key Ctrl+minus')

for i in range(BOARD_HEIGHT):
   for j in range(BOARD_WIDTH):
      if (i,j) in alives:
         print(SQUARE, end='')
      else:
         print(BLANK, end='')
   print()
##############################################

i = 0
try:
   while i<315:
      i += 1
      sleep(.05)
      os.system('clear')

      matrix_to_print = get_matrix(alives, BOARD_HEIGHT, BOARD_WIDTH)
      alives.clear() 
      for i, row in enumerate(matrix_to_print):
         for j, cell in enumerate(row):
            if cell:
               alives.append((i, j))
               print(SQUARE, end='')
            else:
               print(BLANK,end='')
         print()
      print(len(alives))
except KeyboardInterrupt:
   os.system('clear')
   os.system('xdotool key Ctrl+Alt+0')

