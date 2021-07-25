a=int(input())
while(a>0):
    n=int(input())
    b=[]
    for i in range(n):
        e=int(input())
        b.append(e)
    c=0
    k=0
    key=int(input())
    for i in b:
        c+=1
        if i==key:
            print("Present",c)
            k=1
            break
    if k==0:
        print("Not Present",c)
    a-=1
