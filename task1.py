def teen_value(num):
   if num >12 and num< 20 and num!=15 and num!=16:
      return 0
   else:
      return num

def teen_sum(a,b,c):
   return teen_value(a)+teen_value(b)+teen_value(c)

import sys
try:
   a=int(sys.argv[1])
   b=int(sys.argv[2])
   c=int(sys.argv[3])
   print(teen_sum(a,b,c))
except ValueError:
    print("All inputs must be numeric.")

except IndexError:
   print("Exactly 3 numbers are required")




