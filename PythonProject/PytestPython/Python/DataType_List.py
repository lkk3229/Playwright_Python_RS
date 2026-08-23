# Numeric
# String
# List ==> list is a data type that allows multiple values and can be different data types

value = [1, 2, "rahul", 4, 5]

print(value[0])     # Output ==> 1

print(value[-1])    # Output ==> 5,
# -1 denote last value of list

print(value[1:3])  # Output ==> [2, 'rahul']
# 1 - inclusive but 3 is exclusive

value.insert(3, "shetty")
print(value)   # Output ==> [1, 2, 'rahul', 'shetty', 4, 5]

value.append("End")
print(value)   # Output ==> [1, 2, 'rahul', 'shetty', 4, 5, 'End']

value[2]="RAHUL"     # update index 2 value
del value[0]         # delete index 0 value
print(value)     # Output ==> [2, 'RAHUL', 'shetty', 4, 5, 'End']