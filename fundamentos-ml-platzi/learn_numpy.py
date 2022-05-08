import numpy as np

np.array([10, 20, 24, 5, 15])
a = np.array([10, 0, 30, 20, 4, 31, 51, 24, 5, 15, 20, 24, 5, 15])

a[4] # =>  position 4

a[3:] # => desde la position 3

a[3:7] # => desde la position 3 to 7

a[1::4] # =>  print each 4 positions

np.zeros(5) # =>  create 5 elements with 0

np.ones((4, 5)) # row and col

types(ones)

types(ones[3])

np.linspace(3, 10, 5) # 5 elements between 3 and 10 (real numbers)

c = np.array([10, 0, 30, 20, 4, 31, 51, 24, 5, 15, 20, 24, 5, 15])
np.sort(c)

cc = [ ('name', 'S10', ('age', int))]
data = [('Juan', 10), ('Mary', 32), ('James', 29)]
users =  np.array(data, dtype = cc)
np.sort(users, order = 'age')

np.arange(25)

np.arange(5, 50, 5) # elements from 5 to 5, inc = 5

np.full((3,5), 10) # matrx 5,3

np.diag([0,3,9,10]) # matrix diagonal