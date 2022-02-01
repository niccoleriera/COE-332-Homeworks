for i in range(3,101):
    for x in range(2,i):
        if (i%x)==0:
            break
    else:
        print(i)
        
