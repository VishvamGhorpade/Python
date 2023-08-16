print("hey")

def myfunc():
    global x
    x = "cool"
    print("python is "+ x)

myfunc()
print("python is "+ x)
