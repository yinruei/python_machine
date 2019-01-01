# i = 1
# if (i == 0):

#     def  multipliers () :   
#         return [ lambda x : i * x for i in range( 4 )]

#     print([m(2) for m in multipliers()])

# else:
#     def  multipliers () :   
#         return [ lambda x, i=i : i * x for i in range( 4 )]  

#     print([m(2) for m in multipliers()])

from functools import partial
from operator import mul

def  multipliers () : 
    return [partial(mul, i) for i in range( 4 )]

print([m(2) for m in multipliers()])