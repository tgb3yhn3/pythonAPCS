'''
3 4
1 3 5 4
2 8 9 6
10 15 12 13=88
'''
n,m=map(int,input().split())
A=[]#map
AA=[[0]*n for i in range(m)]
P=[]#暫存路線
p=0#總和
min0=999
for i in range(n):
    A.append(list(map(int,input().split())))
for j in range(len(A)):
    for i in range(len(A)[j]):
        if A[j][i]<min0:
            min0=A[j][i]
            P.append(min0)
            AA[j][i]==True
            if A[j+1][i]>A[j][i-1] and A[j-1][i]>A[j][i-1] and A[j][i+1]>A[j][i-1]:
                if AA[j][i-1]==False:
                    P.append(A[j][i-1])
                    A[j][i-1]=A[j][i]
                else:
                    continue
            elif A[j+1][i]>A[j][i+1] and A[j-1][i]>A[j][i+1] and A[j][i-1]>A[j][i+1]:
                if AA[j][i+1]==False:
                    P.append(A[j][i+1])
                    A[j][i+1]=A[j][i]
                else:
                    continue
            elif A[j+1][i]>A[j-1][i] and A[j][i+1]>A[j-1][i] and A[j][i-1]>A[j-1][i]:
                if AA[j-1][i]==False:
                    P.append(A[j-1][i])
                    A[j-1][i]=A[j][i]
                else:
                    continue
            elif A[j-1][i]>A[j+1][i] and A[j][i+1]>A[j+1][i] and A[j][i-1]>A[j+1][i]:
                if AA[j+1][i]==False:
                    P.append(A[j+1][i])
                    A[j+1][i]=A[j][i]
                else:
                    continue
for i in range(P):
    p+=i
print(p)
'''
for j in range(len(A)):
    for i in range(len(A)[j]):
        if A[j][i]<min0:
            min0=A[j][i]
            P.append(min0)
            if A[j+1][i]>A[j][i-1] and A[j-1][i]>A[j][i-1] and A[j][i+1]>A[j][i-1]:
                P.append(A[j][i-1])
                A[j][i-1]=A[j][i]
            elif A[j+1][i]>A[j][i+1] and A[j-1][i]>A[j][i+1] and A[j][i-1]>A[j][i+1]:
                P.append(A[j][i+1])
                A[j][i+1]=A[j][i]
            elif A[j+1][i]>A[j-1][i] and A[j][i+1]>A[j-1][i] and A[j][i-1]>A[j-1][i]:
                P.append(A[j-1][i])
                A[j-1][i]=A[j][i]
            elif A[j-1][i]>A[j+1][i] and A[j][i+1]>A[j+1][i] and A[j][i-1]>A[j+1][i]:
                P.append(A[j+1][i])
                A[j+1][i]=A[j][i]
'''

