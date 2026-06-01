def linearsort(nums,k):
    for i in range(len(nums)):
        if nums[i]==k:
            return i
    return -1
num=[1,2,3,4,45,3,4,6,7,7]
keys=45
print(linearsort(num,keys))
