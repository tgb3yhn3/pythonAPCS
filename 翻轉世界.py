def fen0(n):#翻轉
    for j in range(len(n)):
        for i in range(len(n[j])):
            n[j][i],n[len(n)-j-1][len(n[j])-i-1]=n[len(n)-j-1][len(n[j])-i-1],n[j][i]
t=int(input())
while t!=0:
    n,m=map(int,input().split())
    a=[]
    for k in range(n):
        a.append([int(x) for x in input().split()])
    for j in range(len(a)):
        for i in range(len(a[j]):
            if a[j][k]<=1:
                if fen0(a)==a:
                    print("go forward")
                else:
                    print("keep defending")
            else:
                continue
    t-=1
#n=[[1,2,3,4],
      #[5,6,7,8],
      #[9,10,11,12]]
