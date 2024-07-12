total = 0
count = 0

while True :
    val = input("Enter a Number :")

    if val == "done" :
        break

    try :
        fval = float(val)

    except :
        print("Invalid Input")
        continue

    total = total + fval
    count = count + 1

print("Total is :", total)
print("count is :", count )
print("Average is :", total/count)





