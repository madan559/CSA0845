from array import *

pp=array('i',[]) 

n=int(input("Enter the number of elements:"))
if n> 0:
  for i in range(n):
    x=int(input("Enter the element:"))
    pp.append(x)
  odd=0
  even=0
  for i in pp:
       if i%2==0:
           even = even + i**2
       else:
           odd = odd + i**2
  k=[odd,even]
  print(k)
else:
 print("invalid")
