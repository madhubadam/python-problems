arr=[1,2,3,45,5,1,2,34,45,3]
freq={}
for i in range(len(arr)):
    if arr[i] in freq:
        freq[arr[i]]+=1
    else:
        freq[arr[i]]=1
for key in freq:
    print(key)
#rint(len(freq))