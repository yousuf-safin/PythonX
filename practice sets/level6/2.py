marks1 = int(input("Enter Marks 1 :"))
marks2 = int(input("Enter Marks 2 :"))
marks3 = int(input("Enter Marks 3 :"))
marks4 = int(input("Enter Marks 4 :"))
marks5 = int(input("Enter Marks 5 :"))

#Check for total percentage

total_percentage = (100)*(marks1 + marks2 + marks3 + marks4 + marks5)/500

if(total_percentage>=40):
    print("You are pass", total_percentage)
else:
    print("You are fail, try again later",total_percentage)
