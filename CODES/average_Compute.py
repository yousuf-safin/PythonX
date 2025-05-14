# a = int(input("Enater a Number : "))
# b = int(input("Enater a Number : "))

# avg = (a+b)/2
# print("Average Number is :",avg)

n= int(input("Enter the number of terms :"))
total=0
for i in range(n):
    num = int(input(f"Enter Number {i+1}: "))
    total += num
avg= total/n
print ("average number is : ",avg)