print("hello")

# for commenting

a = 3
print(a)

Str = "Hello World"
print(Str)

b, c, d = 5, 6.4, "Great"

print(a, b, c, d, Str)
# Output ==> 3 5 6.4 Great Hello World

# print("value is"+b)  ==> TypeError: can only concatenate str (not "int") to str

print("{}{}".format("Value is ", b))
# Output ==> Value is 5

print(type(c))
# Output ==> <class 'float'>

