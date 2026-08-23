val = (1, 2, "rahul", 4, 5)
print(val[1])   #Output ==> 2

#val[2] = "shetty"
#print(val)    TypeError: 'tuple' object does not support item assignment


dic = {"a":2, 4:"bcd", "c":"Hello", "d":4}
print(dic[4])    # output ==> bcd
# here 4 is the key and output bcd is value

print(dic["c"])   # Output ==> Hello

# create a new dictionary
dict = {}
dict["firstname"] = "Rahul"
dict["lastname"] = "Haran"
dict["age"] = 25
dict["gender"] = "male"
print(dict["firstname"])
print(dict["lastname"])
print(dict["age"])
print(dict["gender"])
print(dict)
