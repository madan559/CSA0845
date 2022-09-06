def add(x,y):
    return x+y
def subtrct(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return (x%y)
select=int(input("select the operation 1,2,3,4:"))
number_1=int(input("enter the first number:"))
number_2=int(input("enter the second number:"))
if select==1:
    print(number_1,"+",number_2,"=",(number_1+number_2))
elif select==2:
    print(number_1,"_",number_2,"=",(nmber_1-number_2))
elif select==3:
    print(number_1,"*",number_2,"=",(number_1*number_2))
elif select==4:
    print(number_1,"%",number_2,"=",(number_1%number_2))
else:
    print("invalid")
