# a=3
# b=4
# print(a+b)
# print(b%a)



# # z=int(input("Enter a Number :"))
# # print(type(z))

# # comparison
# print(a>b)

# x= int(input("Enter a Number :"))
# y= int(input("Enter a Number :"))
# r= x+y
# print("Avg is",r/2)
# print("Square of a number",x*x)

m= input("Enter a Satring :")
if "  " in m:
    print("Double Space detected")
    corct= m.replace("  "," ")
    print(corct)
else:
    print("No Double Space Detected")


print(f'"Good Girl is {m}"')

letter='''
Dear, <Name>
You are selected!
<Date>
'''
letter=letter.replace("<Name>","Yousuf")
letter=letter.replace("<Date>","Today")
print(letter)

f= input("My Name : ")
print("My name is",f)