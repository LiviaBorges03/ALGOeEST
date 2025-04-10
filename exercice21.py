nums=[]
print("Digite 10 numeros:")
for i in range (10):
    numero= int(input(f"Digite o {i + 1} número: "))
    nums.append(numero)

soma=0

for numero in nums:
    soma = soma+numero

print("A soma de todos os numeros é:", soma)