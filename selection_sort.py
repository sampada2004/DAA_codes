def selection(a):
    for i in range(len(a)-1):
        min=i
        for j in range(i+1,len(a)):
            if a[min]>a[j]:
                min=j
        a[i],a[min]=a[min],a[i]
print("enter size")
n=int(input("enter "))
print("elements?")
a=[]
for i in range(0,n): 
    m=int(input()) 
    a.append(m)
selection(a)
print("sorted are:")
for i in range(0,n):
    print(a[i])              