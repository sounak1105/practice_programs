#dec_to_binary
def decimal_binary():
    a = int(input("enter a number"))
    b= 0
    c=0
    b=a%2
    c=c+b
    i=1
    a=int(a/2)
    while (a>0):
        b=a%2
        c=b*(10**i)+c
        a=int(a/2)
        i+=1
    print(c)

decimal_binary()