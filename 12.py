l=[54,16,89,1,62,7,18]
n=len(l)
for i in range(n):
    print("Pass:", i+1)
    for j in range(n-1-i):
        if(l[j] > l[j+1]):
            l[j], l[j+1] = l[j+1], l[j]
        print(l)
