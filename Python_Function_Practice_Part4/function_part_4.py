# one find the maximum of 3 numbers
def max_num(*args):
    return max(args)
print (max_num(27, 346, 86))

# two multiply all the numbers in a list
def mult_list(*args):
    product = 1
    for i in args:
        product = product * i
    return product

print(mult_list(2,5,7,10))

# three reverse a string
def rev_string(myStr):
    return myStr[::-1]

print(rev_string("cat in the hat"))

# four check if a number falls in a given range
def num_within(n):
    if n in range(21,81):
        print(" %s is in the range"%str(n))
    else: 
        print (" %s is not in the range"%str(n))

num_within(21)

# five print out the first n rows of Pascal's triange
def pascal(n):
   for i in range(n+1):
      for j in range(n-i):
         print(end='')

      C = 1
      for j in range(1, i+1):
         print(C, sep='', end='')
         C = C * (i - j) // j
      print()

pascal(4)