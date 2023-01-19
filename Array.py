'''
#1D aaray
num = int(input("Enter the number of size:"))
arr = []

for i in range(num):
    element = int(input("Enter the element"))

    arr.append(element)

print("Number of elements",arr)
'''
'''
#2D Array
r_num = int(input("Enter the row number"))
c_num = int(input("Enter the column number"))

array = [[0 for col in range(c_num)] for row in range(r_num)]

for row in range(r_num):
    for col in range(c_num):
        array[row][col] = row*col
    
print(array)
'''

'''
tot = int(input("Enter the size of an array:"))

arr = []

for i in range(tot):
    while True:
        value = int(input())

        arr.append(value)
        break

print(arr)
while True:   
    try:
        if value in arr:
            val_del = int(input("Enter the element you want to delete:"))
            arr.remove(val_del)
            print(arr)
            break
    except:
        print("Element not found.")

'''
'''
temp = 0
arr = [40,10,30,20]

print("Original array")
for i in range(0,len(arr)):
    print(arr[i])

for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if (arr[i]>arr[j]):
            temp = arr[i]
            arr[i]=arr[j]
            arr[j]= temp

print("\n================================")
print("New Array")
for i in range(0,len(arr)):
    print(arr[i])
'''
arr = [1,2,1,3,4,5,5]

for i in range(0,len(arr)):
    print(arr[i])


value = int(input())
if value in arr:
    print('your value is exist in ',arr.index(value),"Value:",value)

else:
    print('your value is not found')