# use of array to calculate with multiple numbers
def array():
    calc_multiple = [5, '/', 2.5, '+', 5, '*', 14, '/', 7, '*', 3, '+', 50, '-', 2]
    sol=0
    count=0
    while(count<=(len(calc_multiple)-1)):
        if (calc_multiple[count] == '/'):
            sol=calc_multiple[count-1]/calc_multiple[count+1]
            calc_multiple.pop(count-1)
            calc_multiple.pop(count-1)
            calc_multiple.pop(count-1)
            calc_multiple.insert(count-1,sol)
            count=0
        count+=1
    count=0
    while(count<=(len(calc_multiple)-1)):
        if (calc_multiple[count] == '*'):
            sol=calc_multiple[count-1]*calc_multiple[count+1]
            calc_multiple.pop(count-1)
            calc_multiple.pop(count-1)
            calc_multiple.pop(count-1)
            calc_multiple.insert(count-1,sol)
            count=0
        count+=1
    count=0
    while(count<=(len(calc_multiple)-1)):
        if (calc_multiple[count] == '+'):
            sol=calc_multiple[count-1]+calc_multiple[count+1]
            calc_multiple.pop(count-1)
            calc_multiple.pop(count-1)
            calc_multiple.pop(count-1)
            calc_multiple.insert(count-1,sol)
            count=0
        count+=1
    count=0
    while(count<=(len(calc_multiple)-1)):
        if (calc_multiple[count] == '-'):
            sol=calc_multiple[count-1]-calc_multiple[count+1]
            calc_multiple.pop(count-1)
            calc_multiple.pop(count-1)
            calc_multiple.pop(count-1)
            calc_multiple.insert(count-1,sol)
            count=0
        count+=1

    print (calc_multiple)

array()
