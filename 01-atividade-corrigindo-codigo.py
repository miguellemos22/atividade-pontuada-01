import os
os.system("cls || clear")
lista_numeros = []
quantidade_numeros = 5
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
maior_numeros = 0
menor_numeros = 0
soma_pares = 0
soma_impares = 0
soma_geral = 0
for i in range(quantidade_numeros):
    numeros = int(input(f"digite o {i + 1}º numero: "))
    lista_numeros.append(numeros)
    
    if numeros % 2 == 0:
        quantidade_pares += 1
        soma_pares += numeros
        
    else:
        quantidade_impares += 1
        soma_impares += numeros
        
    if numeros < 0:
        quantidade_negativos += 1
    elif numeros > 0:
        quantidade_positivos += 1

maior_numeros = max(lista_numeros)
menor_numeros = min(lista_numeros)

soma_geral += numeros
media_geral = soma_geral / 5
media_pares = soma_pares / quantidade_pares 
media_impares = soma_impares / quantidade_impares 

# Mostrando números na ordem inversa

# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Maior número: {maior_numeros}")
print(f"Menor número: {menor_numeros}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média dos números ímpares: {media_impares:.2f}")
print(f"Média de todos os números: {media_geral:.2f}")

for i,numero in enumerate(reversed(lista_numeros)):
    print(f"{len(lista_numeros)- i} º - {numero}")
