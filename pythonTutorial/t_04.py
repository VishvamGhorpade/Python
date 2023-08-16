#operators
#ARTHEMATIC OPERATORS
x = 3
y = 9
a = x + y #additon
print(a)
b = x - y #subtraction
print(b)
c = x / y #division
print(c)
d = x * y #multiplication
print(d)
e = x % y #modulus to find remainder
print(e)
f = x ** y #power
print(f)
g = x // y #floor division (rounds down to the whole number)
print(g)

#COMPARISON OPERATORS
x = 5
y = 3

print(x == y) #equal to
print(x != y ) #not equal to
print(x > y ) #x greater than y
print(x < y ) #x less than y
print(x >= y ) #x greater than equal to y
print(x <= y) #x lesser than equal to y

#BOOLEAN OPERATORS (LOGICAL OPERATORS)
x = 20
y = 50
print(x<25 and y> 50) #false
print(x<25 or y> 50) #true
print(not(x<25 and y> 50)) #true

#TENARY OPERATOR
def Ifadult(age):
    return True if age <= 18 else False