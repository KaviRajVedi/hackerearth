n = int(input())
a = list(map(int,input().strip().split()))[:n]
b = list(map(int,input().strip().split()))[:n]
k=min(a)
steps=0
flag=True
for i in range(n):
    while(a[i]>k and b[i]!=0):
        a[i]=a[i]-b[i]
        steps+=1
    if(a[i]<0):
        flag=False
    else:
        k=a[i]
for i in a:
    if(i!=min(a)):
        flag=False
print("-1") if flag == False else print(steps)
