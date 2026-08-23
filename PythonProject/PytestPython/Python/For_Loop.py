#for loop
obj = [2, 3, 5, 7, 9]
for x in obj:
    print(x)

print("********************************")
for y in obj:
    print(y*2)

print("********************************")

# Sum of first five numbers 1+2+3+4+5=15
# range(i,j) ==> i to j-1
summation=0
for j in range(1, 6):
    summation += j
print(summation)

print("********************************")
# for (int i=1; i<=10; i+=2)
for i in range(1, 10, 2):
    print(i)

print("********************************")
print("*********Skipping first index***********")
for m in range(10):
    print(m)

print("********************************")
#  for (int i = 10; i >= 0; i -= 3)
for n in range(10, 0, -3):
    print(n)
