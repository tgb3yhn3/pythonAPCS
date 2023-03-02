n,m=map(int,input().split())
u=False
for i in range(n,m+1,1):
    f=str(i)
    r=0
    for j in range(len(f)):
        #f[j]**len(f)
        r=r+int(f[j])**len(f)
    if i==r:
        print(i,end=" ")
        u=True
if u==False:
    print("none")
