def selectionsort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
        
            
    return arr


nums=[24,3,4,44,1,45,67,2,99,31]
print(selectionsort(nums))