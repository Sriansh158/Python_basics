name = "Hello Ravi"
try:
    value =int(name)
except:
    value = -1
print("First",value)

name="123"
try:
    value=int(name)
except:
    value= -2
print("Second", value)