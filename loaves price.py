fresh=int(input("enter the number of fresh loves purchased="))
old=int(input("enter the number of day old loaves purchased="))
if fresh>=0 and old>=0:
 regularprice=185
 freshp=fresh*185
 oldp=(old*185*60)/100
 total=freshp+oldp
 print("regular price:Rs185.00")
 print("amount of new lovaes:",freshp)
 print("amount of day old loaves:",oldp)
 print("total amount:RS.",total)
else:
 print("invalid")
