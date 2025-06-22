mylist = [1,6,3,5,3,4]

ele = int(input("Enter the element to be searched: "))
# flag=0
# for i in mylist:
#     if i == ele:
#         print("Element found")
#         flag=1
#         break
# if flag==0:
#     print("Element not found")

if ele in mylist:
    print("Element found")
else:
    print("Element not found")