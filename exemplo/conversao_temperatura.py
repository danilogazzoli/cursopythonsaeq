print("---- Converta uma temperatura (Celsius ou Farenheit) para a outra medida. -------")


temp = input('Entre com uma temperatura. Exemplo 20C ou 100F :')
temp = temp.upper()
tempn = int(temp[:-1]) 


if temp.endswith('C'):
    f=(9*tempn + (32*5)) / 5   
    print(f"A temperatura em Farenheit é: {f} F")
elif temp.endswith('F'): 
    c=(5*(tempn-32))/9
    print(f"A temperatura em Celsius é: {c} C")
else:
    print("Entrada incorreta")