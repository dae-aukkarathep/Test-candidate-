import csv
import random

def Ex01():
  print('Enter your Text:')
  x = input()
  print('Hello, ' + x)

def Ex02():
  with open('D:/Name.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["FirstName"]} {row["LastName"]} ')
        line_count += 1

def Ex03():
  x = random.randint(0,999999)
  x = str(x)
  print ("The winning number is : " + x)
  x = x[4:]
  numbers = []
  for i in range(999999):
    
      p = "{:06}".format(i)
      p = str(p) 
      if  p[4:] == x:
          numbers.append(p) 
  print ("The output array should have : \t")
  print(numbers)

def Ex04():
  x = random.randint(0,999999)
  x = str(x)
  print ("The winning number is : " + x)
  j = 0 
  b = 1
  c = 2
  d = 3
  e = 4
  f = 5
  numbers = []
  r = 6*5*4*3*2*1
  for i in range(r):
      str_num = x[j] + x[b] + x[c] + x[d] + x[e] + x[f]
      numbers.append(str_num)
      f -= 1
      if f < 0 :
          f = 5
      elif f > 5:
          f = 0
      e -= 1
      if e < 0 :
          e = 4
      elif e > 4:
          e = 0
      d -= 1
      if d < 0 :
          d = 3
      elif d > 3:
          d = 0
      c -= 1
      if c < 0 :
          c = 2
      elif c > 2:
          c = 0
      b -= 1
      if b < 0 :
          b = 1
      elif b > 1:
          b = 0
      j += 1
      if j < 0 :
          j = 0
      elif j > 5:
          j = 0
  
  print(len(numbers))
  print(numbers)

Ex01()
Ex02()
Ex03()
Ex04()

