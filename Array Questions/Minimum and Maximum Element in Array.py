def getMinMax(arr, size):
    min_element = arr[0]
    max_element = arr[0]
    
    for i in range(1,size):
        if arr[i] < min_element:
            min_element = arr[i]
        
        if arr[i] > max_element:
            max_element = arr[i]
    
    return min_element, max_element
    


size = int(input("Enter the size of Array : "))
arr = []
for i in range(size):
    arr1 = int(input())
    arr.append(arr1)
print(arr)

min_element, max_element = getMinMax(arr, size)
print("Minimum Element is : ",min_element)
print("Maximum Element is : ",max_element)