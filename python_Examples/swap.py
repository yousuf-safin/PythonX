# num1 = 10
# num2 = 20
num1 = int(input("Enter Number 1 :"))
num2 = int(input("Enter Number 2 :"))

print("Value of Num1 before swapping:",num1)
print("Value of Num2 before swapping:",num2)
#approach 1
# temp = num1
# num1 = num2
# num2 = temp

#approach 2
num1,num2=num2,num1


print("Value of Num1 after swapping:",num1)
print("Value of Num2 after swapping:",num2)