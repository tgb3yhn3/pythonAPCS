'''
3 4
1 3 5 4
2 8 9 6
10 15 12 13=63
'''
n,m=map(int,input().split())
A=[]#map
AA=[[0]*m for i in range(n)]
P=[]#暫存路線
p=0#總和
min0=999
nowi=0
nowj=0
lasti=0
lastj=0
v=[[-1,0],[0,1],[1,0],[0,-1]]
for i in range(n):
    A.append(list(map(int,input().split())))
for j in range(len(A)):
    for i in range(len(A[j])):
        if A[j][i]<min0:
            min0=A[j][i]
            nowi=i
            nowj=j
P.append(min0)
AA[nowi][nowj]=True
while True:
    nexti=nowi#暫存下一個i
    nextj=nowj#暫存下一個j
    lasti=nowi
    lastj=nowj
    tempMin=999999
    for k in v:
        if(0<=nowi+k[0]<n)and(0<=nowj+k[1]<m):#處理要在邊界內
            if(A[nowi+k[0]][nowj+k[1]]<tempMin) and AA[nowi+k[0]][nowj+k[1]]==False:
                nexti=nowi+k[0]
                nextj=nowj+k[1]
                tempMin=A[nowi+k[0]][nowj+k[1]]
    #print(nexti)
    #print(nextj)
    if nowi==nexti and nowj==nextj:
        break
    nowi=nexti
    nowj=nextj
    AA[nowi][nowj]=True
    P.append(A[nowi][nowj])
print(sum(P))
