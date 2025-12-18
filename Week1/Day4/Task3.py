data = []
newData = [1,2,3]

for x in newData:
    data.append(x)
    
print(f"Newly Stored data: {data}")
data.pop(-1)
print(f"After Removing last data new list is:{data}")