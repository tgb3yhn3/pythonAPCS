c,w=map(int,input().split())
r=0#鐵殼蛹#可進化的獨角蟲數量
#c=糖果數量
#w=獨角蟲數量
a=0
while c>=12:
    w-=1
    r+=1
    c-=11#-12+1
    #r=8
if (c+w+r)%12!=0:
    a=(c+w+r)//12
    w-=a
    c+=w+r
    w=(c+w+r)%12
    c=0
    c+=w
    r+=a
print(r)
