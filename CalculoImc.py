altura = float(input('Digite sua altura em cm : '))
peso = float(input('Digite seu peso em KG : '))

IMC = peso / (altura/100)**2

#print(IMC)

if IMC < 18.5:
    print(f'Magreza : {IMC}')

elif IMC >=18.5 and IMC <= 24.9:
    print(f'Normal : {IMC}')

elif  IMC >=25 and IMC <=29.9:
    print(f'Sobrepeso : {IMC}')

elif IMC >= 30 and IMC <=39.9:
    print(f'Obesidade : {IMC}')

else:
    print(f'Obesidade grave : {IMC}')          
