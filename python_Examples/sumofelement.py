arr = [1,2,3,4,5]

print(sum(arr,-10))

# Create an empty list to store the numbers
my_list = []

# Ask the user how many numbers they want to enter
count = int(input("How many numbers do you want to enter? "))

# Loop that many times
for i in range(count):
    # Ask for a number and convert it to an integer
    number = int(input(f"Enter number {i + 1}: "))
    
    # Add the number to our list
    my_list.append(number)

# Print the final list
print("Here is your list:", my_list)
print("The sum of the numbers in the list is:", sum(my_list))