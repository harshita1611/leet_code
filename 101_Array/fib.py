def fib() :
    table=list(range(50))
    table[0]=1
    table[1]=2
    result , count =2,2
    while (True) :
        table[count]=table[count-1] + table[count-2]
        if table[count]>=4000000:
            break
        if (table[count]%2 ==0) :
            result+=table[count]

        count+=1
    return result

print(fib())