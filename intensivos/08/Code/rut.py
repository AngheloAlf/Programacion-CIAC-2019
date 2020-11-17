rut=input('Ingrese numero: ')

cont=len(rut)-1
parcial=0
cont2=0
while cont>=0:
    parcial+= int(rut[cont])*((cont2%6)+2)
    cont2+=1
    cont-=1
parcial%=11
parcial=11-parcial
if parcial==11:
    dv='0'
elif parcial==10:
    dv='k'
else:
    dv=str(parcial)
print('El RUT es '+rut+'-'+dv)
