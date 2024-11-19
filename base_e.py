import math
n=int(input("big chungus. "))
c=""
for i in range (1,n+1):
    c=""
    m=float(i+0.5)
    j= math.floor(math.log(m))
    while j >=0:
        if m/(math.e **j)<1:
            c=c+"0"
        elif m/(math.e**j)<2:
            c=c+"1"
            m=m-math.e**j
        elif m/(math.e**j)<math.e:
            c=c+"2"
            m=m-2*math.e**j
        j=j-1
    print(c)
