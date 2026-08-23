str= "RahulShettyAcademy.com"
str1 = " Cusultancy Firm"
str3 =  "Rahul"

print(str)
print(str[1])
print(str[0:5])   # if you want substring in python

# Output ==> RahulShettyAcademy.com
# a
# Rahul

print(str+str1)   # Output ==> RahulShettyAcademy.com Cusultancy Firm

print(str3 in str) # output ==> True

var = str.split(".")
print(var)    # Output ==> ['RahulShettyAcademy', 'com']
print(var[0])  # Output ==> RahulShettyAcademy

str4= " greet "
print(str4.strip())  # remove both side space
print(str4.lstrip()) # remove left side space
print(str4.rstrip()) # remove right side space
# Output ==> greet
# greet
#  greet