a=int(input())
while(a>0):
    n=int(input())
    b=[]
    for i in range(n):
        e=int(input())
        b.append(e)
    c=0
    k=0
    le=len(b)
    h=l-1e
    lo=0
    mid=(h+lo)//2
    key=int(input())
    for i in range(len(b)):
        c+=1
        if b[mid]==key:
            print("Present",c)
            k=1
            break
        elif b[mid]<key:
            lo=mid+1
        else:
            h=mid-1
        mid=(h+lo)//2
    if k==0:
        print("Not Present",c)
    a-=1
