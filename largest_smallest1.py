largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    
    if num == "done":
        break
    
    try:
        inum = int(num)
    except ValueError:
        print("Invalid input")
        continue
    
    # Initialize largest and smallest on the first valid input
    if largest is None or inum > largest:
        largest = inum
    
    if smallest is None or inum < smallest:
        smallest = inum

print("Maximum is", largest)
print("Minimum is", smallest)
