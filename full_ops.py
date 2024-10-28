# full_ops.py
# Usage:  python3 full_ops.py c_in n_wv

#   determine the output shape and operation count of  a fully-connected layer

# Parameters:
# c_in: input channel count
# n_wv: number of weight vectors

# Output:
#   shape and operation count of a convolution layer
#
# Written by Connor Walsh
# Other contributors: Brad Denby
#

# import Python modules
# e.g., import math # math module
import sys # argv

# "constants"
# e.g., R_E_KM = 6378.137

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
c_in = float('nan') #: input channel count
n_wv = float('nan') #:  number of weight vectors

# parse script arguments
if len(sys.argv)==3:
    c_in = float(sys.argv[1]) #: input channel count
    n_wv = float(sys.argv[2]) #: input width count

else:
  print(\
   'Usage: '\
   'python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p'\
  )
  exit()

# write script below this line

c_out = n_wv
h_out = 1
w_out = 1

adds = n_wv*c_in
muls = n_wv*c_in
divs = 0

print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed