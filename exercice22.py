palavras=[]
for i in range (6):
    palavra=str(input("Digite uma palavra"))
    palavras.append(palavra)
total=0
for palavras in palavra: 
    if (len(palavra))>=5:
        total=total+1
print("total é:", total)