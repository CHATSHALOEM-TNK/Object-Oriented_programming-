def my(a,b):
    for i in range(a,b+1,1):
        if i %3 ==0:
            print(f"{i}")
    ans=my(1,10)
    print(ans)