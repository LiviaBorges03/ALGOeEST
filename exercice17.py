anodenascimento=int(input("Qual o ano do seu nascimento"))
anoatual=int(input("Digite ano atual"))
idadeatual=anoatual-anodenascimento
if idadeatual>= 18:
    print("maior de idade") 
else:
    print("menor de idade")