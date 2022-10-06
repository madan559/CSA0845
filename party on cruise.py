E=[]
L=[]
T=int(input("range T:"))
if T>0 :
 for i in range(T):
    e=input("E:")
    if e!=' ':
      E.append(e)
    else:
     print("invalid")
 for i in range(T):
    l=int(input("L:"))
    L.append(l)
    Sum=0
 Max=0
 for i in range(T):
    Sum+=E[i]-L[i]
    Max=max(Sum,Max)
 print("output",Max)
else:
 print("invalid")
