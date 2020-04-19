max = 20
mid = int(max/2)
string = '+'*max
char = '.'

newList = list(string)
print("".join(newList))
for i in range(0,mid):
    newList[mid-1-i] = char
    newList[mid+i] = char
    print("".join(newList))
    
