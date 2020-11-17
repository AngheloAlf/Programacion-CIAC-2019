#pi
n=int(input('n: ')) #total de ciclos a realizar
suma=0
i=0 #como contador iterativo
while i<n:
    suma+=((-1)**i)/(2*i+1)
    i+=1
print(suma*4)
