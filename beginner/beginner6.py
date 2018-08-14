year = int(input())
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("yes")
       else:
           print("no")
   else:
       print("yes")
else:
   print("no")
