salariobase=float(input("insira seu salario"))
horasextras=float(input("insira o numero de hores extras trabalhadas"))
valorpago=float(input("insira o vaor pago por hora extra"))
valordehoraextra=horasextras*valorpago 
total=salariobase+valordehoraextra
print(f"o valor total do salário{total}")
