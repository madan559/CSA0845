n=int(input("enter the number:"))
factorial=1
if n>=1:
      for i in range(1,n+1):
            factorial=factorial*i
print("factorial of the given number is:",factorial)
