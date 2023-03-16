while True:
    try:
        a,b,c,d,e,f=map(int,input().split())
        if a==0 or b==0 or c==0:
            if a//d==b//e!=c//f :
                print("No answer")
            elif a//d==b//e==c//f:
                print("Too many")
            else:
                y=(f-c*d)/(e-b*d)
                x=((c-b*y)/a)
                print("x=%.2f" %x)
                print("y=%.2f" %y)
        elif d==0 or e==0 or f==0:
            if d//a==e//b!=f//c:
                print("No answer")
            elif d//a==e//b==f//c:
                print("Too many")
            else:
                y=(f-c*d)/(e-b*d)
                x=((c-b*y)/a)
                print("x=%.2f" %x)
                print("y=%.2f" %y)
        elif a!=0 and b!=0 and c!=0 and d!=0 and e!=0 and f!=0:
            if d//a==e//b!=f//c:
                print("No answer")
            elif d//a==e//b==f//c:
                print("Too many")
            else:
                y=(f-c*d)/(e-b*d)
                x=((c-b*y)/a)
                print("x=%.2f" %x)
                print("y=%.2f" %y)
    except:
        break
