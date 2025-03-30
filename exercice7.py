num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
opcao = input("Insira a operação desejada (soma, subtração, multiplicação, divisão): ")
soma = num1 + num2  # Adição
sub = num1 - num2  # Subtração
mult = num1 * num2  # Multiplicação
div = num1 / num2  # Divisão (o resultado será um número decimal se necessário)
if opcao == "soma":  # Se o usuário digitou "soma", mostramos o resultado da soma
    print(f"Resultado: {soma}")

elif opcao == "subtração":  # Se o usuário digitou "subtração", mostramos o resultado da subtração
    print(f"Resultado: {sub}")

elif opcao == "multiplicação":  # Se o usuário digitou "multiplicação", mostramos o resultado da multiplicação
    print(f"Resultado: {mult}")

elif opcao == "divisão":  # Se o usuário digitou "divisão", mostramos o resultado da divisão
    print(f"Resultado: {div}")

else:  
    # Se o usuário digitou algo diferente das opções, exibimos uma mensagem de erro
    print("Operação inválida. Escolha entre: soma, subtração, multiplicação ou divisão.")