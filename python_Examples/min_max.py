arr = [1,2,33,12,4,5]

n= len(arr)
max = arr[0]
for i in range(n):
    if arr[i]>max:
        max = arr[i]
print("Maximum Number is : ",max)

min=arr[0]
for i in range(n):
    if arr[i]<min:
        min = arr[i]
print("Minimum Number is : ",min)