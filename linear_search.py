n=int(input())
a=[]
for i in range(n):
    e=int(input())
    a.append(e)

k=int(input())
for i in range(n):
    if a[i]==k:
        print("found")
