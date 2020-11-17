b1='14,15,16,17\n'
b2='a#3#b#5#c#7'
b3='oh mira4no gracias4un dos tres'
b4='Miguel Godoy#22#4,3,12\n'

b1=list(map(int,b1.strip().split(',')))

lis2=b2.split('#')
b2={}
for i in range(0,6,2):
    b2[lis2[i]]=int(lis2[i+1])

lis3=b3.split('4')
b3=[]
for frase in lis3:
    frase=frase.replace(' ','')
    b3.append((frase,len(frase)))
b3=tuple(b3)

lis4=b4.strip().split('#')
b4=[]
b4.append(lis4[0].split()[0])
b4.append(int(lis4[1]))
b4.append(list(map(int,lis4[2].split(','))))
