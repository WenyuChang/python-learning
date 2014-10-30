number = 10

while number<=23:
    print("number is ", number, ", and less than 23.")
    number=number+1
else:
    print("number has been added to 23.")
    
#===============================================================

# add break, the else block will not arrived
while number<=23:
    print("number is ", number, ", and less than 23.")
    number=number+1
    break
else:
    print("number has been added to 23.")